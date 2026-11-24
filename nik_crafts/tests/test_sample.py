import frappe
from frappe.tests import IntegrationTestCase
from frappe.tests.utils import toggle_test_mode

from nik_crafts.tests import sample


class TestSampleCompany(IntegrationTestCase):
	def test_the_sample_company_is_there_before_the_first_test(self):
		company = frappe.db.get_value(
			"Company", sample.COMPANY, ["country", "default_currency"], as_dict=True
		)

		self.assertEqual(company, {"country": "Austria", "default_currency": "EUR"})
		self.assertTrue(frappe.db.exists("Project", {"customer": "Familie Gruber"}))

	def test_loading_twice_changes_nothing(self):
		customers = frappe.db.count("Customer")

		sample.load()

		self.assertEqual(frappe.db.count("Customer"), customers)

	def test_a_site_without_developer_mode_refuses_outside_tests(self):
		self.addCleanup(setattr, frappe.conf, "developer_mode", frappe.conf.developer_mode)
		self.addCleanup(toggle_test_mode, True)
		frappe.conf.developer_mode = 0
		toggle_test_mode(False)

		self.assertRaises(RuntimeError, sample.load)
