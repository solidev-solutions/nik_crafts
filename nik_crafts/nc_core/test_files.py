"""A file's name keeps the type of the file stored under it."""

import frappe
from frappe.tests import IntegrationTestCase


class TestFiles(IntegrationTestCase):
	def setUp(self):
		super().setUp()
		self.addCleanup(frappe.db.rollback)
		self.file = store("bericht.png")

	def test_a_file_can_be_renamed(self):
		self.file.file_name = "Bericht vom Montag.PNG"

		self.file.save()

		self.assertEqual(frappe.db.get_value("File", self.file.name, "file_name"), "Bericht vom Montag.PNG")

	def test_a_file_cannot_change_its_type(self):
		self.file.file_name = "bericht.html"

		self.assertRaises(frappe.ValidationError, self.file.save)

	def test_a_new_file_takes_the_type_of_the_file_stored_under_it(self):
		self.assertRaises(frappe.ValidationError, store, "bericht.svg")


def store(file_name):
	return frappe.get_doc(
		{"doctype": "File", "file_name": file_name, "content": "Bericht", "is_private": 1}
	).insert()
