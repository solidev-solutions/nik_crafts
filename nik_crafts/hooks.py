app_name = "nik_crafts"
app_title = "NichtImKopf Crafts Community"
app_publisher = "Solidev - Thomas Liska"
app_description = "Business software for small craft businesses, built on ERPNext"
app_email = "contact@solidev.solutions"
app_license = "agpl-3.0-or-later"

required_apps = ["frappe/erpnext@version-16"]

after_install = "nik_crafts.nc_core.setup.after_install"
after_uninstall = "frappe.core.doctype.scheduled_job_type.scheduled_job_type.sync_jobs"
setup_wizard_stages = "nik_crafts.nc_core.setup.stages"

doc_events = {
	"Company": {"on_update": "nik_crafts.nc_core.setup.on_company_update"},
	"File": {"validate": "nik_crafts.nc_core.files.keep_the_type"},
}

permission_query_conditions = {
	"Employee": "nik_crafts.nc_core.permissions.employee_conditions",
	"Timesheet": "nik_crafts.nc_core.permissions.timesheet_conditions",
}
has_permission = {
	"Employee": "nik_crafts.nc_core.permissions.has_employee_permission",
	"Timesheet": "nik_crafts.nc_core.permissions.has_timesheet_permission",
}

user_data_fields = [
	{
		"doctype": "Employee",
		"filter_by": "user_id",
		"redact_fields": [
			"date_of_birth",
			"cell_number",
			"personal_email",
			"prefered_email",
			"current_address",
			"permanent_address",
			"person_to_be_contacted",
			"emergency_phone_number",
			"relation",
			"bank_name",
			"bank_ac_no",
			"passport_number",
			"place_of_issue",
			"family_background",
			"health_details",
		],
	}
]

before_tests = "nik_crafts.tests.sample.load"

ignore_translatable_strings_from = ["frappe", "erpnext"]
