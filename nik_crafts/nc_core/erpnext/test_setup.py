"""What the app relies on in erpnext.setup."""

import frappe
from frappe.tests import IntegrationTestCase

from nik_crafts.nc_core.erpnext import setup


class TestTaxes(IntegrationTestCase):
	def setUp(self):
		super().setUp()
		self.addCleanup(frappe.db.rollback)
		self.company = frappe.defaults.get_global_default("company")
		self.abbr = frappe.db.get_value("Company", self.company, "abbr")

	def test_a_rate_gets_its_account_and_its_template(self):
		setup.create_taxes(self.company, taxes(account_number="2391"), in_use=False)

		self.assertEqual(self.accounts_of_the_template(), [f"2391 - Probesteuer - {self.abbr}"])
		self.assertEqual(
			frappe.db.get_value("Account", f"2391 - Probesteuer - {self.abbr}", "account_type"), "Tax"
		)

	def test_a_company_in_use_gets_no_default_template_from_us(self):
		default = {"company": self.company, "is_default": 1}
		before = frappe.get_all("Sales Taxes and Charges Template", default, pluck="name")

		setup.create_taxes(self.company, taxes(is_default=1), in_use=True)

		self.assertEqual(frappe.get_all("Sales Taxes and Charges Template", default, pluck="name"), before)

	def test_an_account_of_the_business_is_not_taken_for_ours(self):
		group = frappe.db.get_value(
			"Account", {"company": self.company, "account_type": "Tax", "is_group": 1}
		)
		frappe.get_doc(
			{
				"doctype": "Account",
				"company": self.company,
				"parent_account": group,
				"account_name": "Fremdes Konto",
				"account_number": "2391",
			}
		).insert()

		setup.create_taxes(self.company, taxes(account_number="2391"), in_use=True)

		self.assertEqual(self.accounts_of_the_template(), [f"Probesteuer - {self.abbr}"])

	def test_an_input_tax_account_of_a_company_in_use_lands_in_the_group_of_its_chart(self):
		chart_group = frappe.db.get_value("Account", {"company": self.company, "account_number": "1500"})

		setup.create_taxes(self.company, taxes(root_type="Asset"), in_use=True)

		self.assertEqual(
			frappe.db.get_value("Account", f"Probesteuer - {self.abbr}", "parent_account"), chart_group
		)

	def accounts_of_the_template(self):
		template = frappe.get_doc("Sales Taxes and Charges Template", f"Probe - {self.abbr}")
		return [row.account_head for row in template.taxes]


def taxes(is_default=0, **account):
	account = {"account_name": "Probesteuer", "tax_rate": 20.0, **account}
	row = {"account_head": account, "description": "Probesteuer", "rate": 20.0}
	template = {"title": "Probe", "is_default": is_default, "taxes": [row]}
	return {"chart_of_accounts": {"*": {"sales_tax_templates": [template]}}}
