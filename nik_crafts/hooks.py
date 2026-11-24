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

doc_events = {"Company": {"on_update": "nik_crafts.nc_core.setup.on_company_update"}}

before_tests = "nik_crafts.tests.sample.load"

ignore_translatable_strings_from = ["frappe", "erpnext"]
