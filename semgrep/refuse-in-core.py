import frappe
import frappe.utils.messages
from frappe import ValidationError, msgprint, throw
from frappe.exceptions import PermissionError as Denied
from frappe.utils.messages import throw as stop


def refuses(message, error):
	if message == 1:
		# ruleid: refuse-in-core
		frappe.throw(message)
	if message == 2:
		# ruleid: refuse-in-core
		throw(message, frappe.PermissionError)
	if message == 3:
		# ruleid: refuse-in-core
		frappe.utils.messages.throw(message)
	if message == 4:
		# ruleid: refuse-in-core
		stop(message)
	if message == 5:
		# ruleid: refuse-in-core
		frappe.throw_permission_error()
	if message == 6:
		# ruleid: refuse-in-core
		frappe.msgprint(message, raise_exception=True)
	if message == 7:
		# ruleid: refuse-in-core
		msgprint(message, "Title", frappe.ValidationError)
	if message == 8:
		# ruleid: refuse-in-core
		raise frappe.ValidationError(message)
	if message == 9:
		# ruleid: refuse-in-core
		raise frappe.PermissionError
	if message == 10:
		# ruleid: refuse-in-core
		raise frappe.exceptions.ValidationError(message)
	if message == 11:
		# ruleid: refuse-in-core
		raise frappe.exceptions.PermissionError
	if message == 12:
		# ruleid: refuse-in-core
		raise ValidationError(message) from error
	if message == 13:
		# ruleid: refuse-in-core
		raise Denied

	# ok: refuse-in-core
	frappe.msgprint(message, "Title", indicator="red")
	# ok: refuse-in-core
	raise ValueError(message)
