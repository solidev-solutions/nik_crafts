import frappe
import frappe.client
import frappe.model.delete_doc
import requests
from frappe import db, qb
from frappe import get_doc as load
from frappe import local as site
from frappe.model.delete_doc import delete_doc as remove
from frappe.model.document import Document, bulk_insert, get_cached_doc
from frappe.model.mapper import get_mapped_doc
from frappe.model.naming import make_autoname
from frappe.model.rename_doc import rename_doc
from frappe.model.workflow import apply_workflow

# ruleid: database-in-repositories
import frappe.database
# ruleid: database-in-repositories
import frappe.query_builder
# ruleid: database-in-repositories
import pypika
# ruleid: database-in-repositories
from frappe.database import savepoint
# ruleid: database-in-repositories
from frappe.database.database import savepoint as rolls_back
# ruleid: database-in-repositories
from frappe.query_builder.functions import Sum
# ruleid: database-in-repositories
from pypika.terms import Criterion


def database_and_query_builder(name, table):
	# ruleid: database-in-repositories
	frappe.db.get_value("NC Time Entry", name, "minutes")
	# ruleid: database-in-repositories
	handle = frappe.db
	# ruleid: database-in-repositories
	db.count("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.local.db.count("NC Time Entry")
	# ruleid: database-in-repositories
	site.db.count("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.local.primary_db.count("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.local.replica_db.count("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.qb.from_(table).select(table.name).run()
	# ruleid: database-in-repositories
	qb.DocType("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.local.qb.DocType("NC Time Entry")

	# ok: database-in-repositories
	frappe.local.flags
	# ok: database-in-repositories
	frappe.session.user


def document_functions(name, doctype, doc, path):
	# ruleid: database-in-repositories
	frappe.get_doc("NC Time Entry", name)
	# ruleid: database-in-repositories
	load("NC Time Entry", name)
	# ruleid: database-in-repositories
	frappe.get_lazy_doc("NC Time Entry", name)
	# ruleid: database-in-repositories
	frappe.get_cached_doc("NC Time Entry", name)
	# ruleid: database-in-repositories
	frappe.get_last_doc("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.get_single("NC Settings")
	# ruleid: database-in-repositories
	frappe.get_single_value("NC Settings", "rounding")
	# ruleid: database-in-repositories
	frappe.get_cached_value("NC Time Entry", name, "minutes")
	# ruleid: database-in-repositories
	frappe.get_value("NC Time Entry", name, "minutes")
	# ruleid: database-in-repositories
	frappe.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories
	frappe.get_list(doctype)
	# ruleid: database-in-repositories
	frappe.get_all(doctype)
	# ruleid: database-in-repositories
	frappe.new_doc("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.copy_doc(doc)
	# ruleid: database-in-repositories
	frappe.delete_doc("NC Time Entry", name)
	# ruleid: database-in-repositories
	frappe.delete_doc_if_exists("NC Time Entry", name)
	# ruleid: database-in-repositories
	frappe.rename_doc("NC Time Entry", name, "x")
	# ruleid: database-in-repositories
	frappe.import_doc(path)
	# ruleid: database-in-repositories
	frappe.reload_doc("nc_times", "doctype", "nc_time_entry")
	# ruleid: database-in-repositories
	frappe.reload_doctype("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.make_property_setter({"doctype": "Project", "property": "hidden", "value": 1})
	# ruleid: database-in-repositories
	frappe.get_query("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.get_query_builder("mariadb")
	# ruleid: database-in-repositories
	frappe.client.get_value("NC Time Entry", "minutes", name)
	# ruleid: database-in-repositories
	get_cached_doc("NC Time Entry", name)
	# ruleid: database-in-repositories
	Document({"doctype": "NC Time Entry"})
	# ruleid: database-in-repositories
	frappe.model.delete_doc.delete_doc("NC Time Entry", name)
	# ruleid: database-in-repositories
	rename_doc("NC Time Entry", name, "x")
	# ruleid: database-in-repositories
	get_mapped_doc("NC Time Entry", name, {})
	# ruleid: database-in-repositories
	make_autoname("NC-.#####")
	# ruleid: database-in-repositories
	apply_workflow(doc, "Approve")
	# ruleid: database-in-repositories
	frappe.model.create_new.get_new_doc("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.model.db_query.DatabaseQuery("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.model.qb_query.DatabaseQuery("NC Time Entry")

	# ok: database-in-repositories
	frappe.get_meta("NC Time Entry")
	# ok: database-in-repositories
	frappe.has_permission("NC Time Entry", "read", name, throw=True)
	# ok: database-in-repositories
	frappe.defaults.set_user_default("company", name)


def document_methods(doc, rows, pool, image, job, path, url, options):
	# ruleid: database-in-repositories
	doc.insert()
	# ruleid: database-in-repositories
	doc.insert(ignore_if_duplicate=True)
	# ruleid: database-in-repositories
	doc.insert(set_name="x")
	# ruleid: database-in-repositories
	doc.insert(set_child_names=False)
	# ruleid: database-in-repositories
	doc.save()
	# ruleid: database-in-repositories
	doc.save(ignore_version=True)
	# ruleid: database-in-repositories
	doc.delete()
	# ruleid: database-in-repositories
	doc.delete(delete_permanently=True)
	# ruleid: database-in-repositories
	doc.delete(**options)
	# ruleid: database-in-repositories
	doc.submit()
	# ruleid: database-in-repositories
	doc.cancel()
	# ruleid: database-in-repositories
	doc.discard()
	# ruleid: database-in-repositories
	doc.reload()
	# ruleid: database-in-repositories
	doc.load_from_db()
	# ruleid: database-in-repositories
	doc.get_latest()
	# ruleid: database-in-repositories
	doc.db_get("minutes")
	# ruleid: database-in-repositories
	doc.get_db_value("minutes")
	# ruleid: database-in-repositories
	doc.deferred_insert()
	# ruleid: database-in-repositories
	doc.queue_action("submit")
	# ruleid: database-in-repositories
	doc._save()
	# ruleid: database-in-repositories
	doc._submit()
	# ruleid: database-in-repositories
	doc._cancel()

	# ok: database-in-repositories
	rows.insert(0, doc)
	# ok: database-in-repositories
	pool.submit(job, doc)
	# ok: database-in-repositories
	image.save("/tmp/file.png")
	# ok: database-in-repositories
	image.save(fp=path, quality=90)
	# ok: database-in-repositories
	requests.delete(url, options)
	# ok: database-in-repositories
	requests.delete(url, timeout=10)
	# ok: database-in-repositories
	doc.has_value_changed("minutes")


def permission_switches(doc, repository, name, flag, options, user):
	# ruleid: database-in-repositories
	doc.insert(ignore_permissions=True)
	# ruleid: database-in-repositories
	doc.save(ignore_permissions=flag)
	# ruleid: database-in-repositories
	doc.delete(ignore_permissions=1)
	# ruleid: database-in-repositories
	frappe.get_list(
		"NC Time Entry",
		filters={"name": name},
		ignore_permissions=True,
	)
	# ruleid: database-in-repositories
	frappe.get_doc(
		{"doctype": "NC Time Entry"}
	).insert(ignore_permissions=True)
	# ruleid: database-in-repositories
	frappe.get_list("NC Time Entry", ignore_user_permissions=True)


def passes_the_switch_on(doc, ignore_permissions=False):
	# ruleid: database-in-repositories
	doc.insert(ignore_permissions=ignore_permissions)


def switches_by_position(doc, table, image, path, name, flag, args, options):
	# ruleid: database-in-repositories
	doc.insert(flag)
	# ruleid: database-in-repositories
	doc.insert(*args)
	# ruleid: database-in-repositories
	doc.save(**options)
	# ruleid: database-in-repositories
	frappe.delete_doc("NC Time Entry", name, 0, None, True)
	# ruleid: database-in-repositories
	frappe.delete_doc("NC Time Entry", name, for_reload=True)
	# ruleid: database-in-repositories
	frappe.delete_doc_if_exists("NC Time Entry", name, for_reload=True)
	# ruleid: database-in-repositories
	remove("NC Time Entry", name, for_reload=True)
	# ruleid: database-in-repositories
	rename_doc("NC Time Entry", name, "x", validate=False)
	# ruleid: database-in-repositories
	rename_doc("NC Time Entry", name, "x", False, False, True)

	# ruleid: database-in-repositories
	frappe.client.save(doc)
	# ruleid: database-in-repositories
	built_for_later = frappe.qb.into(table).insert(name)


def acts_as_another_user(user, manager, reason):
	# ruleid: database-in-repositories
	frappe.get_list("NC Time Entry", user=user)
	# ruleid: database-in-repositories
	frappe.db.get_list("NC Time Entry", user=user)


def validation_switches(doc, name, options):
	# ruleid: database-in-repositories
	doc.insert(ignore_mandatory=True)
	# ruleid: database-in-repositories
	doc.insert(ignore_links=True)
	# ruleid: database-in-repositories
	frappe.delete_doc("NC Time Entry", name, ignore_on_trash=True)


def writes_past_the_controller(doc, name, entries):
	# ruleid: database-in-repositories
	doc.db_set("minutes", 30)
	# ruleid: database-in-repositories
	doc.db_insert()
	# ruleid: database-in-repositories
	doc.db_update()
	# ruleid: database-in-repositories
	doc.db_update_all()
	# ruleid: database-in-repositories
	doc.update_child_table("entries")
	# ruleid: database-in-repositories
	doc.update_children()
	# ruleid: database-in-repositories
	doc.update_single({"rounding": 15})
	# ruleid: database-in-repositories
	frappe.model.document.bulk_insert("NC Time Entry", entries)
	# ruleid: database-in-repositories
	bulk_insert("NC Time Entry", entries)
	# ruleid: database-in-repositories
	frappe.db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories
	frappe.db.set_single_value("NC Settings", "rounding", 15)
	# ruleid: database-in-repositories
	frappe.db.delete('NC Time Entry', {"name": name})
	# ruleid: database-in-repositories
	frappe.db.truncate("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.db.bulk_insert("NC Time Entry", ["name"], [[name]])
	# ruleid: database-in-repositories
	frappe.db.bulk_update("NC Time Entry", {name: {"minutes": 30}})
	# ruleid: database-in-repositories
	frappe.db.delete(doctype="NC Time Entry")
	# ruleid: database-in-repositories
	db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories
	frappe.local.db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories
	frappe.local.primary_db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories
	frappe.local.replica_db.set_value("NC Time Entry", name, "minutes", 30)


def writes_with_the_query_builder(table, name, query, values, rows):
	# ruleid: database-in-repositories
	frappe.qb.update(table).set(table.minutes, 0).run()
	# ruleid: database-in-repositories
	built_for_later = frappe.qb.update(table).set(table.minutes, 0)
	# ruleid: database-in-repositories
	frappe.qb.into(table).insert(name, 30).run()
	# ruleid: database-in-repositories
	frappe.qb.from_(table).where(table.name == name).delete().run()
	# ruleid: database-in-repositories
	deleted_later = frappe.qb.from_(table).where(table.name == name).delete()
	# ruleid: database-in-repositories
	frappe.qb.get_query("NC Time Entry", delete=True, filters={"name": name})
	# ruleid: database-in-repositories
	frappe.get_query("NC Time Entry", update=True)
	# ruleid: database-in-repositories
	frappe.qb.get_query("NC Time Entry", into=True)
	# ruleid: database-in-repositories
	query.delete().run()


def deletes_and_renames_with_force(doc, name):
	# ruleid: database-in-repositories
	frappe.delete_doc("NC Time Entry", name, force=True)
	# ruleid: database-in-repositories
	frappe.delete_doc_if_exists("NC Time Entry", name, force=1)
	# ruleid: database-in-repositories
	frappe.model.delete_doc.delete_doc("NC Time Entry", name, force=name)
	# ruleid: database-in-repositories
	frappe.delete_doc("NC Time Entry", name, True)
	# ruleid: database-in-repositories
	frappe.delete_doc_if_exists("NC Time Entry", name, True)
	# ruleid: database-in-repositories
	doc.delete(force=True)
	# ruleid: database-in-repositories
	frappe.rename_doc("NC Time Entry", name, "x", force=True)
	# ruleid: database-in-repositories
	frappe.rename_doc("NC Time Entry", name, "x", True)

	# ruleid: database-in-repositories
	frappe.delete_doc("NC Time Entry", name, ignore_missing=False)
	# ruleid: database-in-repositories
	frappe.reload_doc("nc_times", "doctype", "nc_time_entry", force=True)
	# ruleid: database-in-repositories
	frappe.client.rename_doc("NC Time Entry", name, "x", True)


def erpnext_tables(name, doctype, values, own, table):
	# ruleid: database-in-repositories
	frappe.db.set_value("Sales Invoice", name, "status", "Paid")
	# ruleid: database-in-repositories
	frappe.db.set_single_value("Selling Settings", "so_required", "No")
	# ruleid: database-in-repositories
	frappe.db.delete("Timesheet", {"name": name})
	# ruleid: database-in-repositories
	frappe.db.truncate("Timesheet")
	# ruleid: database-in-repositories
	frappe.db.bulk_insert("Project", ["name"], [[name]])
	# ruleid: database-in-repositories
	frappe.db.bulk_update("Project", {name: {"status": "Open"}})
	# ruleid: database-in-repositories
	frappe.db.delete(doctype)
	# ruleid: database-in-repositories
	frappe.db.delete(f"NC {doctype}")
	# ruleid: database-in-repositories
	frappe.db.delete("NC Time Entry" if own else doctype)
	# ruleid: database-in-repositories
	frappe.db.set_value(dt="Sales Invoice", dn=name, field="status", val="Paid")
	# ruleid: database-in-repositories
	frappe.db.delete(doctype="Timesheet")
	# ruleid: database-in-repositories
	frappe.db.set_value(*values)
	# ruleid: database-in-repositories
	db.delete("Timesheet", {"name": name})
	# ruleid: database-in-repositories
	frappe.local.db.delete("Timesheet", {"name": name})
	# ruleid: database-in-repositories
	frappe.local.primary_db.set_value("Sales Invoice", name, "status", "Paid")
	# ruleid: database-in-repositories
	frappe.local.replica_db.delete(doctype)
	# ruleid: database-in-repositories
	frappe.db.sql("select name from `tabNC Time Entry`")
	# ruleid: database-in-repositories
	frappe.db.sql_list("select name from `tabProject`")
	# ruleid: database-in-repositories
	frappe.db.sql_ddl("alter table `tabProject` add column x int")
	# ruleid: database-in-repositories
	frappe.db.multisql({"mariadb": "select 1"})
	# ruleid: database-in-repositories
	frappe.db.execute_query("select 1")
	# ruleid: database-in-repositories
	frappe.local.primary_db.sql("select 1")
	# ruleid: database-in-repositories
	frappe.db.add_index("NC Time Entry", ["project"])
	# ruleid: database-in-repositories
	frappe.db.add_unique("NC Time Entry", ["project"])
	# ruleid: database-in-repositories
	frappe.db.rename_column("NC Time Entry", "minutes", "duration")
	# ruleid: database-in-repositories
	frappe.db.rename_table("NC Time Entry", "NC Booking")
	# ruleid: database-in-repositories
	frappe.db.change_column_type("NC Time Entry", "minutes", "int")
	# ruleid: database-in-repositories
	frappe.db.updatedb("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.db.create_sequence("NC Time Entry")
	# ruleid: database-in-repositories
	frappe.db.set_next_sequence_val("NC Time Entry", 1)

	# ruleid: database-in-repositories
	frappe.qb.update(frappe.qb.DocType("Sales Invoice")).set("status", "Paid")
	# ruleid: database-in-repositories
	frappe.get_doc("Sales Invoice", name).db_set("status", "Paid")
	# ruleid: database-in-repositories
	frappe.db.get_value("Sales Invoice", name, "status")


def rollbacks(handle):
	# ruleid: database-in-repositories
	frappe.db.rollback(save_point="before_booking")

	# ruleid: database-in-repositories
	frappe.db.savepoint("before_booking")
