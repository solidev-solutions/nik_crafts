from pathlib import Path

import frappe
from frappe.desk.page.setup_wizard.setup_wizard import setup_complete
from frappe.utils import getdate

COMPANY = "Musterbetrieb GmbH"


def load():
	if not (frappe.conf.developer_mode or frappe.in_test):
		raise RuntimeError("The sample company is for development and tests only.")
	if frappe.db.exists("Company", COMPANY):
		return
	if frappe.is_setup_complete():
		raise RuntimeError("The sample company needs a site whose setup has not run yet.")

	# The wizard switches the running process to German, which would leave the caller in it.
	lang = frappe.local.lang
	year = getdate().year
	setup_complete(
		{
			"language": "Deutsch",
			"country": "Austria",
			"timezone": "Europe/Vienna",
			"currency": "EUR",
			"company_name": COMPANY,
			"company_abbr": "MB",
			"chart_of_accounts": "Standard with Numbers",
			"fy_start_date": f"{year}-01-01",
			"fy_end_date": f"{year}-12-31",
		}
	)
	frappe.local.lang = lang

	for path in sorted(Path(__file__).parent.glob("*.json")):
		for record in frappe.get_file_json(path):
			frappe.get_doc(record).insert()
