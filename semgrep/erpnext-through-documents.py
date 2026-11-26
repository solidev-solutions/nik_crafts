import frappe
from frappe import db


def erpnext_tables(name, doctype, values, own, table):
	# ruleid: erpnext-through-documents
	frappe.db.set_value("Sales Invoice", name, "status", "Paid")
	# ruleid: erpnext-through-documents
	frappe.db.set_single_value("Selling Settings", "so_required", "No")
	# ruleid: erpnext-through-documents
	frappe.db.delete("Timesheet", {"name": name})
	# ruleid: erpnext-through-documents
	frappe.db.truncate("Timesheet")
	# ruleid: erpnext-through-documents
	frappe.db.bulk_insert("Project", ["name"], [[name]])
	# ruleid: erpnext-through-documents
	frappe.db.bulk_update("Project", {name: {"status": "Open"}})
	# ruleid: erpnext-through-documents
	frappe.db.delete(doctype)
	# ruleid: erpnext-through-documents
	frappe.db.delete(f"NC {doctype}")
	# ruleid: erpnext-through-documents
	frappe.db.delete("NC Time Entry" if own else doctype)
	# ruleid: erpnext-through-documents
	frappe.db.set_value(dt="Sales Invoice", dn=name, field="status", val="Paid")
	# ruleid: erpnext-through-documents
	frappe.db.delete(doctype="Timesheet")
	# ruleid: erpnext-through-documents
	frappe.db.set_value(*values)
	# ruleid: erpnext-through-documents
	db.delete("Timesheet", {"name": name})
	# ruleid: erpnext-through-documents
	frappe.local.db.delete("Timesheet", {"name": name})
	# ruleid: erpnext-through-documents
	frappe.local.primary_db.set_value("Sales Invoice", name, "status", "Paid")
	# ruleid: erpnext-through-documents
	frappe.local.replica_db.delete(doctype)
	# ruleid: erpnext-through-documents
	frappe.db.sql("select name from `tabNC Time Entry`")
	# ruleid: erpnext-through-documents
	frappe.db.sql_list("select name from `tabProject`")
	# ruleid: erpnext-through-documents
	frappe.db.sql_ddl("alter table `tabProject` add column x int")
	# ruleid: erpnext-through-documents
	frappe.db.multisql({"mariadb": "select 1"})
	# ruleid: erpnext-through-documents
	frappe.db.execute_query("select 1")
	# ruleid: erpnext-through-documents
	frappe.local.primary_db.sql("select 1")
	# ruleid: erpnext-through-documents
	frappe.db.add_index("NC Time Entry", ["project"])
	# ruleid: erpnext-through-documents
	frappe.db.add_unique("NC Time Entry", ["project"])
	# ruleid: erpnext-through-documents
	frappe.db.rename_column("NC Time Entry", "minutes", "duration")
	# ruleid: erpnext-through-documents
	frappe.db.rename_table("NC Time Entry", "NC Booking")
	# ruleid: erpnext-through-documents
	frappe.db.change_column_type("NC Time Entry", "minutes", "int")
	# ruleid: erpnext-through-documents
	frappe.db.updatedb("NC Time Entry")
	# ruleid: erpnext-through-documents
	frappe.db.create_sequence("NC Time Entry")
	# ruleid: erpnext-through-documents
	frappe.db.set_next_sequence_val("NC Time Entry", 1)

	# ok: erpnext-through-documents
	frappe.cache.set_value("Sales Invoice", name)
