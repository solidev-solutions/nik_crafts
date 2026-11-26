"""A worker sees only their own employee record and their own timesheets, the office sees all of them."""

import frappe
from frappe.client import set_value
from frappe.tests import IntegrationTestCase

WORKER = "lukas.berger@musterbetrieb.example"
COLLEAGUE = "stefan.bauer@musterbetrieb.example"
OFFICE = "sabine.wagner@musterbetrieb.example"


class TestOwnRecords(IntegrationTestCase):
	def setUp(self):
		super().setUp()
		self.addCleanup(frappe.cache.hdel, "user_permissions", WORKER)
		self.addCleanup(frappe.db.rollback)
		self.worker_record = frappe.db.get_value("Employee", {"user_id": WORKER})
		self.colleague_record = frappe.db.get_value("Employee", {"user_id": COLLEAGUE})
		# The worker's User Permission would hide the colleague too.
		frappe.get_doc("User Permission", {"user": WORKER, "allow": "Employee"}).delete()

	def test_a_worker_sees_only_their_own_employee_record(self):
		with self.set_user(WORKER):
			listed = frappe.get_list("Employee", pluck="name")
			reads_own = frappe.has_permission("Employee", doc=self.worker_record)
			reads_colleague = frappe.has_permission("Employee", doc=self.colleague_record)

		self.assertIn(self.worker_record, listed)
		self.assertNotIn(self.colleague_record, listed)
		self.assertTrue(reads_own)
		self.assertFalse(reads_colleague)

	def test_the_office_sees_every_employee_record(self):
		with self.set_user(OFFICE):
			listed = frappe.get_list("Employee", pluck="name")
			reads_colleague = frappe.has_permission("Employee", doc=self.colleague_record)

		self.assertIn(self.colleague_record, listed)
		self.assertTrue(reads_colleague)

	def test_a_worker_sees_only_their_own_timesheets(self):
		own_timesheet = book_time(self.worker_record)
		colleague_timesheet = book_time(self.colleague_record)

		with self.set_user(WORKER):
			listed = frappe.get_list("Timesheet", pluck="name")
			reads_own = frappe.has_permission("Timesheet", doc=own_timesheet)
			reads_colleague = frappe.has_permission("Timesheet", doc=colleague_timesheet)

		self.assertIn(own_timesheet, listed)
		self.assertNotIn(colleague_timesheet, listed)
		self.assertTrue(reads_own)
		self.assertFalse(reads_colleague)

	def test_the_office_sees_every_timesheet(self):
		colleague_timesheet = book_time(self.colleague_record)

		with self.set_user(OFFICE):
			listed = frappe.get_list("Timesheet", pluck="name")
			reads_colleague = frappe.has_permission("Timesheet", doc=colleague_timesheet)

		self.assertIn(colleague_timesheet, listed)
		self.assertTrue(reads_colleague)

	def test_a_worker_cannot_take_over_a_colleagues_timesheet(self):
		colleague_timesheet = book_time(self.colleague_record)

		with self.set_user(WORKER):
			self.assertRaises(
				frappe.PermissionError,
				set_value,
				"Timesheet",
				colleague_timesheet,
				"employee",
				self.worker_record,
			)

	def test_a_worker_cannot_hand_their_timesheet_to_a_colleague(self):
		own_timesheet = book_time(self.worker_record)

		with self.set_user(WORKER):
			self.assertRaises(
				frappe.PermissionError,
				set_value,
				"Timesheet",
				own_timesheet,
				"employee",
				self.colleague_record,
			)

	def test_a_worker_cannot_amend_a_colleagues_timesheet(self):
		cancelled = frappe.get_doc("Timesheet", book_time(self.colleague_record))
		cancelled.time_logs[0].activity_type = frappe.get_all("Activity Type", pluck="name", limit=1)[0]
		cancelled.submit()
		cancelled.cancel()

		with self.set_user(WORKER):
			self.assertRaises(
				frappe.PermissionError, book_time, self.worker_record, amended_from=cancelled.name
			)

	def test_a_timesheet_without_an_employee_belongs_to_whoever_booked_it(self):
		with self.set_user(WORKER):
			own_timesheet = book_time(None)
			listed = frappe.get_list("Timesheet", pluck="name")
		with self.set_user(COLLEAGUE):
			reads_for_colleague = frappe.has_permission("Timesheet", doc=own_timesheet)

		self.assertIn(own_timesheet, listed)
		self.assertFalse(reads_for_colleague)


def book_time(employee, **values):
	timesheet = frappe.get_doc(
		{
			"doctype": "Timesheet",
			"employee": employee,
			"time_logs": [{"from_time": "2026-11-24 08:00:00", "hours": 1}],
			**values,
		}
	).insert()
	return timesheet.name
