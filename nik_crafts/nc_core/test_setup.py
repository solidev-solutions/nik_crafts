"""The start data reaches the site, the company of the setup wizard and every company created after it."""

import frappe
from frappe.core.doctype.file.exceptions import FileTypeNotAllowed
from frappe.tests import IntegrationTestCase
from frappe.utils import set_request
from frappe.www.login import send_login_link

from nik_crafts.nc_core import setup

WORKER = "lukas.berger@musterbetrieb.example"


class TestSetup(IntegrationTestCase):
	def test_the_wizard_sets_up_the_settings_and_the_taxes(self):
		company = frappe.defaults.get_global_default("company")

		self.assertEqual(frappe.db.get_single_value("System Settings", "date_format"), "dd.mm.yyyy")
		self.assertEqual(frappe.db.get_single_value("System Settings", "number_format"), "#.###,##")
		self.assertFalse(frappe.db.get_single_value("System Settings", "allow_error_traceback"))
		self.assertTrue(frappe.db.get_single_value("Accounts Settings", "enable_immutable_ledger"))
		self.assertEqual(frappe.db.get_single_value("Website Settings", "auto_account_deletion"), 0)
		self.assertEqual(default_templates(company), ["Umsatzsteuer 20 %", "Vorsteuer 20 %"])

	def test_a_company_created_later_gets_its_taxes(self):
		self.addCleanup(frappe.db.rollback)
		company = frappe.get_doc(
			{
				"doctype": "Company",
				"company_name": "Zweitbetrieb GmbH",
				"abbr": "ZB",
				"country": "Austria",
				"default_currency": "EUR",
				"chart_of_accounts": "Standard with Numbers",
			}
		)

		company.insert()

		self.assertEqual(default_templates(company.name), ["Umsatzsteuer 20 %", "Vorsteuer 20 %"])

	def test_each_person_has_exactly_the_roles_of_their_profiles(self):
		company = frappe.defaults.get_global_default("company")
		users = frappe.get_all("Employee", {"company": company, "user_id": ("is", "set")}, pluck="user_id")
		persons = [frappe.get_doc("User", user) for user in users]
		start_profiles = {
			record["role_profile"] for record in setup.read("site") if record["doctype"] == "Role Profile"
		}

		self.assertEqual(
			{row.role_profile for person in persons for row in person.role_profiles}, start_profiles
		)
		for person in persons:
			expected = set().union(
				*(roles_of("Role Profile", row.role_profile) for row in person.role_profiles)
			)
			self.assertEqual(roles_of("User", person.name), expected, person.name)

	def test_a_profile_the_business_changed_stays_as_it_is(self):
		self.addCleanup(frappe.db.rollback)
		profile = frappe.get_doc("Role Profile", "Büro")
		profile.set("roles", profile.roles[:1])
		profile.save()

		setup.set_up_site()

		self.assertEqual(roles_of("Role Profile", "Büro"), {profile.roles[0].role})

	def test_a_setter_the_business_made_stays_its_own(self):
		self.addCleanup(frappe.db.rollback)
		protection = {
			"doctype": "Quotation",
			"doctype_or_field": "DocType",
			"property": "protect_attached_files",
		}
		frappe.make_property_setter({**protection, "value": 1}, is_system_generated=False)

		setup.set_up_site()

		self.assertIsNone(
			frappe.db.get_value("Property Setter", "Quotation-main-protect_attached_files", "module")
		)

	def test_a_worker_may_not_upload_a_public_file(self):
		self.addCleanup(frappe.db.rollback)
		file = frappe.new_doc("File", file_name="preise.csv", content="Montagestunde;65", is_private=0)

		with self.set_user(WORKER):
			self.assertRaises(frappe.PermissionError, file.insert)

	def test_a_worker_may_not_upload_an_html_file(self):
		self.addCleanup(frappe.db.rollback)
		# Frappe checks the type only of a file that arrives with a request.
		set_request(method="POST", path="/")
		self.addCleanup(delattr, frappe.local, "request")
		file = frappe.new_doc("File", file_name="seite.html", content="<p>Seite</p>", is_private=1)

		with self.set_user(WORKER):
			self.assertRaises(FileTypeNotAllowed, file.insert)

	def test_no_login_link_is_sent(self):
		self.addCleanup(frappe.db.rollback)
		frappe.get_doc(
			{
				"doctype": "Email Account",
				"email_account_name": "Büro",
				"email_id": "buero@musterbetrieb.example",
				"enable_outgoing": 1,
				"default_outgoing": 1,
				"smtp_server": "smtp.musterbetrieb.example",
				"no_smtp_authentication": 1,
			}
		).insert()
		queued = frappe.db.count("Email Queue")

		send_login_link(WORKER)

		self.assertEqual(frappe.db.count("Email Queue"), queued)

	def test_submitted_documents_keep_their_files(self):
		protected = [
			doctype
			for doctype in setup.PROTECTED_ATTACHMENTS
			if frappe.get_meta(doctype).protect_attached_files
		]

		self.assertEqual(protected, setup.PROTECTED_ATTACHMENTS)


def roles_of(doctype, name):
	return {row.role for row in frappe.get_doc(doctype, name).roles}


def default_templates(company):
	return [
		frappe.db.get_value(doctype, {"company": company, "is_default": 1}, "title")
		for doctype in ("Sales Taxes and Charges Template", "Purchase Taxes and Charges Template")
	]
