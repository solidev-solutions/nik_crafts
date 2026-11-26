"""Start data: settings with the first setup, taxes for every company."""

from pathlib import Path

import frappe
from frappe import _

from nik_crafts.nc_core.erpnext.setup import create_taxes

START_DATA = Path(__file__).parent / "start_data"


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
	"""The app arrives on a site that is already set up. Its settings stay as they are."""
	for company in frappe.get_all("Company", pluck="name"):
		set_up_company(company, in_use=True)


def on_company_update(doc, _method):
	"""A company created after the setup. The wizard's company is left to our stage."""
	if doc.flags.in_insert and not frappe.flags.in_setup_wizard:
		set_up_company(doc.name, in_use=False)


def set_up_company(company, *, in_use):
	code = country_code(frappe.db.get_value("Company", company, "country"))
	if taxes := read(f"taxes_{code}"):
		create_taxes(company, taxes, in_use=in_use)


def country_code(country):
	return frappe.db.get_value("Country", country, "code")


def read(name):
	path = START_DATA / f"{name}.json"
	return frappe.get_file_json(path) if path.exists() else {}
