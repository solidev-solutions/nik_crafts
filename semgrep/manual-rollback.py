import frappe
from frappe.database import savepoint
from frappe.database.database import savepoint as rolls_back


def rollbacks(handle):
	# ruleid: manual-rollback
	frappe.db.rollback(save_point="before_booking")
	# ruleid: manual-rollback
	handle.rollback()
	# ruleid: manual-rollback
	with savepoint(catch=frappe.DuplicateEntryError):
		pass
	# ruleid: manual-rollback
	with rolls_back():
		pass


# ruleid: manual-rollback
@savepoint(catch=Exception)
def rolls_back_when_it_fails(doc):
	pass
