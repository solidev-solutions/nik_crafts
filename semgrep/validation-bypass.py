import frappe
import frappe.model.delete_doc
import requests
from frappe import db, flags
from frappe.model.delete_doc import delete_doc as remove
from frappe.model.document import bulk_insert
from frappe.model.rename_doc import rename_doc


def document_methods(doc, rows, pool, image, job, path, url, options):

	# ok: validation-bypass
	requests.delete(url, options)
	# ok: validation-bypass
	options.delete("key", "other")


def switches_by_position(doc, table, image, path, name, flag, args, options):
	# ruleid: validation-bypass
	frappe.delete_doc("NC Time Entry", name, 0, None, True)
	# ruleid: validation-bypass
	frappe.delete_doc("NC Time Entry", name, for_reload=True)
	# ruleid: validation-bypass
	frappe.delete_doc_if_exists("NC Time Entry", name, for_reload=True)
	# ruleid: validation-bypass
	remove("NC Time Entry", name, for_reload=True)
	# ruleid: validation-bypass
	rename_doc("NC Time Entry", name, "x", validate=False)
	# ruleid: validation-bypass
	doc.rename("x", validate_rename=False)
	# ruleid: validation-bypass
	doc._rename("x", validate_rename=False)
	# ruleid: validation-bypass
	rename_doc("NC Time Entry", name, "x", False, False, True)

	# ruleid: validation-bypass
	built_for_later = frappe.qb.into(table).insert(name)
	# ruleid: validation-bypass
	table.insert(name, 30, 40).run()


def validation_switches(doc, name, options):
	# ruleid: validation-bypass
	doc.flags.ignore_validate = True
	# ruleid: validation-bypass
	doc.flags.ignore_validate_update_after_submit = True
	# ruleid: validation-bypass
	frappe.flags.ignore_route_conflict_validation = True
	# ruleid: validation-bypass
	doc.flags.ignore_mandatory = True
	# ruleid: validation-bypass
	doc.insert(ignore_mandatory=True)
	# ruleid: validation-bypass
	doc.insert(ignore_links=True)
	# ruleid: validation-bypass
	doc.ignore_linked_doctypes = ("NC Time Entry",)
	# ruleid: validation-bypass
	frappe.delete_doc("NC Time Entry", name, ignore_on_trash=True)
	# ruleid: validation-bypass
	options["ignore_validate"] = True
	# ruleid: validation-bypass
	frappe.flags.in_import = True
	# ruleid: validation-bypass
	flags.in_install = "nik_crafts"
	# ruleid: validation-bypass
	frappe.flags.update({"in_import": True})
	# ruleid: validation-bypass
	frappe.flags.update(in_import=True)
	# ruleid: validation-bypass
	frappe.flags["in_import"] = True
	# ruleid: validation-bypass
	setattr(frappe.flags, "in_install", True)
	# ruleid: validation-bypass
	options.setdefault("ignore_mandatory", True)

	# ok: validation-bypass
	in_import = frappe.flags.in_import or frappe.flags.get("in_install")
	# ok: validation-bypass
	ignore_links_on_delete = ["NC Time Entry"]


# ruleid: validation-bypass
def passes_a_validation_switch_on(doc, ignore_links=False):
	return doc


def writes_past_the_controller(doc, name, entries):
	# ruleid: validation-bypass
	doc.db_set("minutes", 30)
	# ruleid: validation-bypass
	doc.db_insert()
	# ruleid: validation-bypass
	doc.db_update()
	# ruleid: validation-bypass
	doc.db_update_all()
	# ruleid: validation-bypass
	doc.update_child_table("entries")
	# ruleid: validation-bypass
	doc.update_children()
	# ruleid: validation-bypass
	doc.update_single({"rounding": 15})
	# ruleid: validation-bypass
	frappe.model.document.bulk_insert("NC Time Entry", entries)
	# ruleid: validation-bypass
	bulk_insert("NC Time Entry", entries)
	# ruleid: validation-bypass
	frappe.db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: validation-bypass
	frappe.db.set_single_value("NC Settings", "rounding", 15)
	# ruleid: validation-bypass
	frappe.db.delete('NC Time Entry', {"name": name})
	# ruleid: validation-bypass
	frappe.db.truncate("NC Time Entry")
	# ruleid: validation-bypass
	frappe.db.bulk_insert("NC Time Entry", ["name"], [[name]])
	# ruleid: validation-bypass
	frappe.db.bulk_update("NC Time Entry", {name: {"minutes": 30}})
	# ruleid: validation-bypass
	frappe.db.delete(doctype="NC Time Entry")
	# ruleid: validation-bypass
	db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: validation-bypass
	frappe.local.db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: validation-bypass
	frappe.local.primary_db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: validation-bypass
	frappe.local.replica_db.set_value("NC Time Entry", name, "minutes", 30)


def writes_with_the_query_builder(table, name, query, values, rows):
	# ruleid: validation-bypass
	frappe.qb.update(table).set(table.minutes, 0).run()
	# ruleid: validation-bypass
	built_for_later = frappe.qb.update(table).set(table.minutes, 0)
	# ruleid: validation-bypass
	frappe.qb.into(table).insert(name, 30).run()
	# ruleid: validation-bypass
	frappe.qb.from_(table).where(table.name == name).delete().run()
	# ruleid: validation-bypass
	deleted_later = frappe.qb.from_(table).where(table.name == name).delete()
	# ruleid: validation-bypass
	frappe.qb.get_query("NC Time Entry", delete=True, filters={"name": name})
	# ruleid: validation-bypass
	frappe.get_query("NC Time Entry", update=True)
	# ruleid: validation-bypass
	frappe.qb.get_query("NC Time Entry", into=True)
	# ruleid: validation-bypass
	table.update().set(table.minutes, 0).where(table.name == name).run()
	# ruleid: validation-bypass
	query.delete().run()

	# ok: validation-bypass
	values.update({"minutes": 30})


def deletes_and_renames_with_force(doc, name):
	# ruleid: validation-bypass
	frappe.delete_doc("NC Time Entry", name, force=True)
	# ruleid: validation-bypass
	frappe.delete_doc_if_exists("NC Time Entry", name, force=1)
	# ruleid: validation-bypass
	frappe.model.delete_doc.delete_doc("NC Time Entry", name, force=name)
	# ruleid: validation-bypass
	frappe.delete_doc("NC Time Entry", name, True)
	# ruleid: validation-bypass
	frappe.delete_doc_if_exists("NC Time Entry", name, True)
	# ruleid: validation-bypass
	doc.delete(force=True)
	# ruleid: validation-bypass
	frappe.rename_doc("NC Time Entry", name, "x", force=True)
	# ruleid: validation-bypass
	frappe.rename_doc("NC Time Entry", name, "x", True)
	# ruleid: validation-bypass
	doc.rename("x", force=True)
	# ruleid: validation-bypass
	doc.rename("x", False, True)
	# ruleid: validation-bypass
	doc._rename("x", False, True)


def erpnext_tables(name, doctype, values, own, table):
	# ruleid: validation-bypass
	frappe.db.set_value("Sales Invoice", name, "status", "Paid")
	# ruleid: validation-bypass
	frappe.db.set_single_value("Selling Settings", "so_required", "No")
	# ruleid: validation-bypass
	frappe.db.delete("Timesheet", {"name": name})
	# ruleid: validation-bypass
	frappe.db.truncate("Timesheet")
	# ruleid: validation-bypass
	frappe.db.bulk_insert("Project", ["name"], [[name]])
	# ruleid: validation-bypass
	frappe.db.bulk_update("Project", {name: {"status": "Open"}})
	# ruleid: validation-bypass
	frappe.db.delete(doctype)
	# ruleid: validation-bypass
	frappe.db.delete(f"NC {doctype}")
	# ruleid: validation-bypass
	frappe.db.delete("NC Time Entry" if own else doctype)
	# ruleid: validation-bypass
	frappe.db.set_value(dt="Sales Invoice", dn=name, field="status", val="Paid")
	# ruleid: validation-bypass
	frappe.db.delete(doctype="Timesheet")
	# ruleid: validation-bypass
	frappe.db.set_value(*values)
	# ruleid: validation-bypass
	db.delete("Timesheet", {"name": name})
	# ruleid: validation-bypass
	frappe.local.db.delete("Timesheet", {"name": name})
	# ruleid: validation-bypass
	frappe.local.primary_db.set_value("Sales Invoice", name, "status", "Paid")
	# ruleid: validation-bypass
	frappe.local.replica_db.delete(doctype)

	# ruleid: validation-bypass
	frappe.qb.update(frappe.qb.DocType("Sales Invoice")).set("status", "Paid")
	# ruleid: validation-bypass
	frappe.get_doc("Sales Invoice", name).db_set("status", "Paid")
