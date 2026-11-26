import frappe
from frappe import whitelist
from frappe.model.document import Document


# ruleid: endpoint-names-methods
@frappe.whitelist()
def unchecked(entry: str):
	return entry


# ruleid: endpoint-names-methods
@frappe.whitelist()
def unchecked_with_a_parameter_named_self(self, entry: str):
	return entry


def plain(entry: str):
	return entry


# ruleid: endpoint-names-methods
whitelisted_by_call = frappe.whitelist()(plain)


# ruleid: endpoint-names-methods
kept_without_a_call = frappe.whitelist


# ruleid: endpoint-names-methods
@frappe.whitelist(allow_guest=True)
def names_no_method(entry: str):
	return entry


# ruleid: endpoint-names-methods
@whitelist()
def names_no_method_and_imported(entry: str):
	return entry


@frappe.read_only()
# ruleid: endpoint-names-methods
@frappe.whitelist()
def names_no_method_below_a_second_decorator(entry: str):
	return entry


# ruleid: endpoint-names-methods
kept_without_a_method = frappe.whitelist(allow_guest=True)

ALLOWED = ["POST"]
OPTIONS = {"methods": ["POST"]}


class NCSiteVisit(Document):
	# ruleid: endpoint-names-methods
	@frappe.whitelist()
	def names_no_method(self):
		return self.name

	# ruleid: endpoint-names-methods
	@frappe.whitelist(methods=[])
	def names_an_empty_list(self):
		return self.name

	# ruleid: endpoint-names-methods
	@frappe.whitelist(methods=ALLOWED)
	def names_a_list_made_elsewhere(self):
		return self.name

	# ruleid: endpoint-names-methods
	@frappe.whitelist(methods=["GET", "POST"])
	def names_two_methods(self):
		return self.name

	# ruleid: endpoint-names-methods
	@frappe.whitelist(methods=["PUT"])
	def names_another_method(self):
		return self.name

	# ruleid: endpoint-names-methods
	@frappe.whitelist(methods=("POST",))
	def names_its_method_in_a_tuple(self):
		return self.name

	# ruleid: endpoint-names-methods
	@frappe.whitelist(methods=["post"])
	def names_its_method_in_lower_case(self):
		return self.name

	# ruleid: endpoint-names-methods
	@frappe.whitelist(False, False, ["POST"])
	def names_its_method_by_position(self):
		return self.name

	# ruleid: endpoint-names-methods
	@frappe.whitelist(**OPTIONS)
	def takes_its_arguments_from_a_dict(self):
		return self.name

	# ok: endpoint-names-methods
	@frappe.whitelist(methods=["POST"])
	def names_post(self):
		return self.name

	# ok: endpoint-names-methods
	@frappe.whitelist(allow_guest=True, methods=["GET"])
	def names_get(self):
		return self.name
