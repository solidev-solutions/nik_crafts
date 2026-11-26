app_name = "nik_crafts"
app_title = "NichtImKopf Crafts Community"
app_publisher = "Solidev - Thomas Liska"
app_description = "Business software for small craft businesses, built on ERPNext"
app_email = "contact@solidev.solutions"
app_license = "agpl-3.0-or-later"

required_apps = ["frappe/erpnext"]

after_uninstall = "frappe.core.doctype.scheduled_job_type.scheduled_job_type.sync_jobs"

before_tests = "nik_crafts.tests.sample.load"

ignore_translatable_strings_from = ["frappe", "erpnext"]
