"""Whoever may not change employee records sees only their own record and their own timesheets."""

import frappe
from frappe.permissions import get_role_permissions


def employee_conditions(user):
	if may_change_employee_records(user):
		return ""
	return f"`tabEmployee`.`user_id` = {frappe.db.escape(user)}"


def has_employee_permission(doc, user):
	return may_change_employee_records(user) or doc.user_id == user


def timesheet_conditions(user):
	if may_change_employee_records(user):
		return ""
	user = frappe.db.escape(user)
	booked_for = f"`tabTimesheet`.`employee` in (select `name` from `tabEmployee` where `user_id` = {user})"
	booked_by = f"ifnull(`tabTimesheet`.`employee`, '') = '' and `tabTimesheet`.`owner` = {user}"
	return f"({booked_for} or ({booked_by}))"


def has_timesheet_permission(doc, user):
	if may_change_employee_records(user):
		return True
	stored = (stored_timesheet(doc.name), stored_timesheet(doc.amended_from))
	return is_own_timesheet(doc, user) and all(not row or is_own_timesheet(row, user) for row in stored)


def stored_timesheet(name):
	return name and frappe.db.get_value("Timesheet", name, ["employee", "owner"], as_dict=True)


def is_own_timesheet(timesheet, user):
	if timesheet.employee:
		return frappe.db.get_value("Employee", timesheet.employee, "user_id") == user
	return timesheet.owner == user


def may_change_employee_records(user):
	# Not frappe.has_permission: without a document one record shared with the user would make it true.
	return bool(get_role_permissions("Employee", user=user).get("write"))
