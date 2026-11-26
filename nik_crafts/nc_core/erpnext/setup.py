"""What the app asks of erpnext.setup."""

import copy

import frappe
from erpnext.setup.setup_wizard.operations.taxes_setup import from_detailed_data
from frappe.translate import print_language


def create_taxes(company, taxes, *, in_use):
	"""Tax accounts and templates from ERPNext's detailed form: for each chart of accounts, sales and
	purchase templates whose rows name their account as a dict.

	ERPNext's function is made for a new company: it saves without validation and takes any account
	that carries our name or our number. On a company in use none of our templates becomes a default,
	and an account with our number but another name stays the business's own.
	"""
	taxes = copy.deepcopy(taxes)
	for chart in taxes["chart_of_accounts"].values():
		for template in chart.get("sales_tax_templates", []) + chart.get("purchase_tax_templates", []):
			if in_use:
				template["is_default"] = 0
			for row in template["taxes"]:
				leave_number_to_its_owner(company, row["account_head"])

	language = frappe.db.get_single_value("System Settings", "language") if in_use else None
	with print_language(language):
		from_detailed_data(company, taxes)


def leave_number_to_its_owner(company, account):
	number = account.get("account_number")
	owner = {"company": company, "account_number": number, "account_name": ("!=", account["account_name"])}
	if number and frappe.db.exists("Account", owner):
		del account["account_number"]
