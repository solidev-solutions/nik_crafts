"""The start data reaches the company of the setup wizard and every company created after it."""

import frappe
from frappe.tests import IntegrationTestCase


class TestSetup(IntegrationTestCase):
	def test_the_wizard_sets_up_the_settings_and_the_taxes(self):
		company = frappe.defaults.get_global_default("company")

		self.assertEqual(frappe.db.get_single_value("System Settings", "date_format"), "dd.mm.yyyy")
		self.assertEqual(frappe.db.get_single_value("System Settings", "number_format"), "#.###,##")
		self.assertTrue(frappe.db.get_single_value("Accounts Settings", "enable_immutable_ledger"))
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


def default_templates(company):
	return [
		frappe.db.get_value(doctype, {"company": company, "is_default": 1}, "title")
		for doctype in ("Sales Taxes and Charges Template", "Purchase Taxes and Charges Template")
	]
