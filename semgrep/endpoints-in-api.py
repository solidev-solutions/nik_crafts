import frappe
from frappe import whitelist
from frappe.model.document import Document


# ruleid: endpoints-in-api
@frappe.whitelist()
def unchecked(entry: str):
	return entry


# ruleid: endpoints-in-api
@whitelist(methods=["POST"])
def unchecked_and_imported(entry: str):
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist()
def unchecked_with_a_parameter_named_self(self, entry: str):
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_without_throw(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry)
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_too_late(entry: str):
	entry = entry.strip()
	frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_in_a_branch(entry: str):
	if entry:
		frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_a_named_user(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry, user="Administrator", throw=True)
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_a_user_by_position(entry: str):
	"""Preview the entry."""
	frappe.has_permission("NC Time Entry", "write", entry, "Administrator", throw=True)
	return entry


def plain(entry: str):
	return entry


# ruleid: endpoints-in-api
whitelisted_by_call = frappe.whitelist()(plain)
# ruleid: endpoints-in-api
kept_for_later = frappe.whitelist(methods=["POST"])


@kept_for_later
def whitelisted_by_a_variable(entry: str):
	return entry


# ruleid: endpoints-in-api
kept_without_a_call = frappe.whitelist


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_only_if_given(entry: str):
	entry and frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_only_if_empty(entry: str):
	entry or frappe.has_permission("NC Time Entry", "write", throw=True)
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_in_one_branch(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry, throw=True) if entry else None
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checked(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checked_below_its_docstring(entry: str):
	"""Preview the entry."""
	frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoints-in-api
@frappe.whitelist(methods=["GET"])
@frappe.read_only()
def checked_below_two_decorators(entry: str):
	frappe.has_permission("NC Time Entry", "read", entry, throw=True)
	return entry


class NCTimeEntry(Document):
	# ok: endpoints-in-api
	@frappe.whitelist()
	def preview(self):
		return self.minutes
