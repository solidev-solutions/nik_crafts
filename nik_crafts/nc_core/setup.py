"""Start data: settings with the first setup, records of the site with the install, taxes for every company."""

from pathlib import Path

import frappe
from frappe import _

from nik_crafts.nc_core.erpnext.setup import create_taxes

START_DATA = Path(__file__).parent / "start_data"

# Frappe lets whoever attached a file or may change its document delete it after the submit. The PDF
# filed when a document is issued and the supplier's invoice belong to the books, so these keep theirs.
PROTECTED_ATTACHMENTS = ["Sales Invoice", "Purchase Invoice", "Quotation", "Sales Order", "Dunning"]


def stages(answers):
	failed = _("The setup of NichtImKopf Crafts failed")
	task = {"fn": set_up_from_wizard, "args": answers, "fail_msg": failed}
	return [{"status": _("Setting up NichtImKopf Crafts"), "fail_msg": failed, "tasks": [task]}]


def set_up_from_wizard(answers):
	"""Our stage of the setup wizard, after ERPNext's stages. Only here the app changes settings."""
	code = country_code(answers.country)
	for name in ("settings", f"settings_{code}"):
		for doctype, values in read(name).items():
			settings = frappe.get_single(doctype)
			settings.update(values)
			# nosemgrep: permission-bypass -- a System Manager may finish the wizard without the role that writes Accounts Settings
			settings.save(ignore_permissions=True)
	set_up_company(answers.company_name, in_use=False)


def after_install():
	"""The app arrives on a fresh site or on one in use. Its settings stay as they are."""
	# Only during the install does a Role Profile update its users at once. Elsewhere it locks itself
	# for a job after the commit, and a failed wizard would leave that lock behind for its next try.
	set_up_site()
	for company in frappe.get_all("Company", pluck="name"):
		set_up_company(company, in_use=True)


def on_company_update(doc, _method):
	"""A company created after the setup. The wizard's company is left to our stage."""
	# ERPNext builds the chart of accounts in Company.on_update, which runs after after_insert.
	if doc.flags.in_insert and not frappe.flags.in_setup_wizard:
		set_up_company(doc.name, in_use=False)


def set_up_site():
	for record in read("site"):
		insert_if_missing(frappe.get_doc(record))
	for doctype in PROTECTED_ATTACHMENTS:
		protect_attached_files(doctype)


def insert_if_missing(doc):
	"""A record with this name belongs to the business and is left as it is.

	insert(ignore_if_duplicate=True) is no way to skip it: it still inserts the rows of the child tables.
	The name must come from the record's own fields: a series, a counter or a hash names it anew each time.
	"""
	doc.set_new_name()
	if not frappe.db.exists(doc.doctype, doc.name):
		doc.insert()


def protect_attached_files(doctype):
	# Inserting ours would delete a setter the business made, which would then leave with ours at the
	# uninstall. Once the business turns the protection off, no setter is left, so a re-install turns
	# it on again.
	if not frappe.db.exists("Property Setter", {"doc_type": doctype, "property": "protect_attached_files"}):
		frappe.make_property_setter(
			{
				"doctype": doctype,
				"doctype_or_field": "DocType",
				"property": "protect_attached_files",
				"value": 1,
				"property_type": "Check",
			},
			validate_fields_for_doctype=False,
			module="NC Core",
		)


def set_up_company(company, *, in_use):
	code = country_code(frappe.db.get_value("Company", company, "country"))
	if taxes := read(f"taxes_{code}"):
		create_taxes(company, taxes, in_use=in_use)


def country_code(country):
	return frappe.db.get_value("Country", country, "code")


def read(name):
	path = START_DATA / f"{name}.json"
	return frappe.get_file_json(path) if path.exists() else {}
