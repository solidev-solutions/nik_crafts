import frappe
from frappe import whitelist
from frappe.model.document import Document


# ruleid: endpoint-checks-permission
@frappe.whitelist()
def unchecked(entry: str):
	return entry


# ruleid: endpoint-checks-permission
@whitelist(methods=["POST"])
def unchecked_and_imported(entry: str):
	return entry


# ruleid: endpoint-checks-permission
@frappe.whitelist()
def unchecked_with_a_parameter_named_self(self, entry: str):
	return entry


# ruleid: endpoint-checks-permission
@frappe.whitelist(methods=["POST"])
def checks_without_throw(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry)
	return entry


# ruleid: endpoint-checks-permission
@frappe.whitelist(methods=["POST"])
def checks_too_late(entry: str):
	entry = entry.strip()
	frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoint-checks-permission
@frappe.whitelist(methods=["POST"])
def checks_in_a_branch(entry: str):
	if entry:
		frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoint-checks-permission
@frappe.whitelist(methods=["POST"])
def checks_a_named_user(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry, user="Administrator", throw=True)
	return entry


# ruleid: endpoint-checks-permission
@frappe.whitelist(methods=["POST"])
def checks_a_user_by_position(entry: str):
	"""Preview the entry."""
	frappe.has_permission("NC Time Entry", "write", entry, "Administrator", throw=True)
	return entry


def plain(entry: str):
	return entry


# ruleid: endpoint-checks-permission
whitelisted_by_call = frappe.whitelist()(plain)
# ruleid: endpoint-checks-permission
kept_for_later = frappe.whitelist(methods=["POST"])


@kept_for_later
def whitelisted_by_a_variable(entry: str):
	return entry


# ruleid: endpoint-checks-permission
kept_without_a_call = frappe.whitelist


# ruleid: endpoint-checks-permission
@frappe.whitelist(methods=["POST"])
def checks_only_if_given(entry: str):
	entry and frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoint-checks-permission
@frappe.whitelist(methods=["POST"])
def checks_only_if_empty(entry: str):
	entry or frappe.has_permission("NC Time Entry", "write", throw=True)
	return entry


# ruleid: endpoint-checks-permission
@frappe.whitelist(methods=["POST"])
def checks_in_one_branch(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry, throw=True) if entry else None
	return entry


class NCTimeEntry(Document):
	# ok: endpoint-checks-permission
	@frappe.whitelist(methods=["GET"])
	def preview(self):
		return self.minutes


# ruleid: endpoint-checks-permission
@frappe.whitelist(allow_guest=True)
def names_no_method(entry: str):
	return entry


# ruleid: endpoint-checks-permission
@whitelist()
def names_no_method_and_imported(entry: str):
	return entry


# ruleid: endpoint-checks-permission
@frappe.read_only()
@frappe.whitelist()
def names_no_method_below_a_second_decorator(entry: str):
	return entry


# ruleid: endpoint-checks-permission
whitelisted_by_call_with_its_method = frappe.whitelist(methods=["POST"])(plain)

# ruleid: endpoint-checks-permission
kept_without_a_method = frappe.whitelist(allow_guest=True)
