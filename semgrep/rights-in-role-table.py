import frappe
from frappe.permissions import get_roles


def roles(user):
	# ruleid: rights-in-role-table
	if "Projects Manager" in frappe.get_roles():
		return True
	# ruleid: rights-in-role-table
	get_roles(user)
	# ruleid: rights-in-role-table
	frappe.get_user().get_roles()
	# ruleid: rights-in-role-table
	frappe.only_for("System Manager")
	# ok: rights-in-role-table
	return frappe.has_permission("NC Time Entry", "write")
