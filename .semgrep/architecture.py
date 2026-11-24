import frappe
import frappe.client
import frappe.model.delete_doc
import frappe.utils.messages
import requests
from frappe import ValidationError, db, flags, msgprint, qb, throw, whitelist
from frappe import get_doc as load
from frappe import local as site
from frappe.core.doctype.user.user import impersonate
from frappe.exceptions import PermissionError as Denied
from frappe.model.delete_doc import delete_doc as remove
from frappe.model.document import Document, bulk_insert, get_cached_doc
from frappe.model.mapper import get_mapped_doc
from frappe.model.naming import make_autoname
from frappe.model.rename_doc import rename_doc
from frappe.model.workflow import apply_workflow
from frappe.permissions import get_roles
from frappe.utils.messages import throw as stop

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

# ruleid: tests-are-not-imported
import nik_crafts.nc_times.application.test_support
# ruleid: tests-are-not-imported
from nik_crafts.nc_times.application import (
	book_time,
	test_support as support,
)
# ruleid: tests-are-not-imported
from nik_crafts.nc_times.application.test_support import helper
# ok: tests-are-not-imported
from frappe.tests import IntegrationTestCase


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
	# ruleid: database-in-repositories, permission-bypass
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

	# ok: database-in-repositories, permission-bypass
	rows.insert(0, doc)
	# ok: database-in-repositories
	pool.submit(job, doc)
	# ok: database-in-repositories, permission-bypass
	image.save("/tmp/file.png")
	# ok: database-in-repositories
	image.save(fp=path, quality=90)
	# ok: database-in-repositories, permission-bypass, validation-bypass
	requests.delete(url, options)
	# ok: database-in-repositories
	requests.delete(url, timeout=10)
	# ok: permission-bypass, validation-bypass
	options.delete("key", "other")
	# ok: database-in-repositories
	doc.has_value_changed("minutes")


def permission_switches(doc, repository, name, flag, options, user):
	# ruleid: database-in-repositories, permission-bypass
	doc.insert(ignore_permissions=True)
	# ruleid: database-in-repositories, permission-bypass
	doc.save(ignore_permissions=flag)
	# ruleid: database-in-repositories, permission-bypass
	doc.delete(ignore_permissions=1)
	# ruleid: database-in-repositories, permission-bypass
	frappe.get_list(
		"NC Time Entry",
		filters={"name": name},
		ignore_permissions=True,
	)
	# ruleid: database-in-repositories, permission-bypass
	frappe.get_doc(
		{"doctype": "NC Time Entry"}
	).insert(ignore_permissions=True)
	# ruleid: permission-bypass
	repository.insert_entry(doc, ignore_permissions=True)
	# ruleid: permission-bypass
	doc.flags.ignore_permissions = flag
	# ruleid: permission-bypass
	frappe.flags.ignore_permissions = True
	# ruleid: permission-bypass
	doc.flags.update({"ignore_permissions": True})
	doc.flags.update(
		# ruleid: permission-bypass
		{
			"name": name,
			"ignore_permissions": True,
		}
	)
	# ruleid: permission-bypass
	options["ignore_permissions"] = True
	# ruleid: permission-bypass
	setattr(doc.flags, "ignore_permissions", True)
	# ruleid: permission-bypass
	options.setdefault("ignore_permissions", True)
	# ruleid: permission-bypass
	doc.flags.ignore_permlevel_for_fields = ["rate"]
	# ruleid: database-in-repositories, permission-bypass
	frappe.get_list("NC Time Entry", ignore_user_permissions=True)
	# ruleid: permission-bypass
	frappe.flags.ignore_user_permissions_for_doctype = "NC Time Entry"
	# ruleid: permission-bypass
	frappe.share.add("NC Time Entry", name, user, flags={"ignore_share_permission": True})
	# ruleid: permission-bypass
	frappe.flags.ignore_print_permissions = True
	# ruleid: permission-bypass
	frappe.local.flags.ignore_select_perm = True

	# ok: permission-bypass
	frappe.has_permission("NC Time Entry", "read", name, ignore_share_permissions=True)
	# ok: permission-bypass
	if doc.flags.ignore_permissions or options.pop("ignore_permissions", None):
		return


# ruleid: permission-bypass
def passes_the_switch_on(doc, ignore_permissions=False):
	# ruleid: database-in-repositories, permission-bypass
	doc.insert(ignore_permissions=ignore_permissions)


def passes_the_switch_on_in_many_lines(
	doc,
	# ruleid: permission-bypass
	ignore_permissions: bool = False,
):
	return doc


def switches_by_position(doc, table, image, path, name, flag, args, options):
	# ruleid: database-in-repositories, permission-bypass
	doc.insert(flag)
	# ruleid: database-in-repositories, permission-bypass
	doc.insert(*args)
	# ruleid: permission-bypass
	doc.insert(None, None, False, True)
	# ruleid: permission-bypass
	doc.insert(True, True)
	# ruleid: permission-bypass
	doc.insert(False, True)
	# ruleid: permission-bypass
	doc.insert(None, True)
	# ruleid: permission-bypass
	doc.save(flag)
	# ruleid: permission-bypass
	doc.save(*args)
	# ruleid: database-in-repositories, permission-bypass
	doc.save(**options)
	# ruleid: permission-bypass
	doc.delete(flag)
	# ruleid: permission-bypass
	doc.delete(False, True)
	# ruleid: permission-bypass
	image.save(path)
	# ruleid: database-in-repositories, permission-bypass, validation-bypass
	frappe.delete_doc("NC Time Entry", name, 0, None, True)
	# ruleid: database-in-repositories, permission-bypass, validation-bypass
	frappe.delete_doc("NC Time Entry", name, for_reload=True)
	# ruleid: database-in-repositories, permission-bypass, validation-bypass
	frappe.delete_doc_if_exists("NC Time Entry", name, for_reload=True)
	# ruleid: database-in-repositories, permission-bypass, validation-bypass
	remove("NC Time Entry", name, for_reload=True)
	# ruleid: database-in-repositories, permission-bypass, validation-bypass
	rename_doc("NC Time Entry", name, "x", validate=False)
	# ruleid: permission-bypass, validation-bypass
	doc.rename("x", validate_rename=False)
	# ruleid: permission-bypass, validation-bypass
	doc._rename("x", validate_rename=False)
	# ruleid: database-in-repositories, permission-bypass, validation-bypass
	rename_doc("NC Time Entry", name, "x", False, False, True)

	# ok: permission-bypass
	doc.insert(flag, True)
	# ok: permission-bypass
	frappe.cache.delete(name)
	# ruleid: database-in-repositories
	frappe.client.save(doc)
	# ruleid: database-in-repositories, validation-bypass
	built_for_later = frappe.qb.into(table).insert(name)
	# ruleid: validation-bypass
	table.insert(name, 30, 40).run()


def acts_as_another_user(user, manager, reason):
	# ruleid: database-in-repositories, permission-bypass
	frappe.get_list("NC Time Entry", user=user)
	# ruleid: database-in-repositories, permission-bypass
	frappe.db.get_list("NC Time Entry", user=user)
	# ruleid: permission-bypass
	frappe.session.user = user
	# ruleid: permission-bypass
	frappe.local.session.user = user
	# ruleid: permission-bypass
	site.session.user = user
	# ruleid: permission-bypass
	frappe.session["user"] = user
	# ruleid: permission-bypass
	frappe.local.session["user"] = user
	# ruleid: permission-bypass
	frappe.session.update({"user": user})
	# ruleid: permission-bypass
	frappe.local.session.update(user=user)
	# ruleid: permission-bypass
	frappe.local.session = frappe._dict(user=user)
	# ruleid: permission-bypass
	manager.login_as(user)
	# ruleid: permission-bypass
	manager.login_as_guest()
	# ruleid: permission-bypass
	manager.impersonate(user)
	# ruleid: permission-bypass
	impersonate(user, reason)

	# ok: permission-bypass
	if frappe.session.user == user:
		return frappe.has_permission("NC Time Entry", "read", user=user)


def excepted(doc, repository):
	# nosemgrep: permission-bypass -- fixture for the comment above a statement
	doc.flags.ignore_permissions = True
	# nosemgrep: permission-bypass -- fixture for the comment above a call of many lines
	repository.insert_entry(
		doc,
		ignore_permissions=True,
	)


def validation_switches(doc, name, options):
	# ruleid: validation-bypass
	doc.flags.ignore_validate = True
	# ruleid: validation-bypass
	doc.flags.ignore_validate_update_after_submit = True
	# ruleid: validation-bypass
	frappe.flags.ignore_route_conflict_validation = True
	# ruleid: validation-bypass
	doc.flags.ignore_mandatory = True
	# ruleid: database-in-repositories, validation-bypass
	doc.insert(ignore_mandatory=True)
	# ruleid: database-in-repositories, validation-bypass
	doc.insert(ignore_links=True)
	# ruleid: validation-bypass
	doc.ignore_linked_doctypes = ("NC Time Entry",)
	# ruleid: database-in-repositories, validation-bypass
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
	# ruleid: database-in-repositories, validation-bypass
	doc.db_set("minutes", 30)
	# ruleid: database-in-repositories, validation-bypass
	doc.db_insert()
	# ruleid: database-in-repositories, validation-bypass
	doc.db_update()
	# ruleid: database-in-repositories, validation-bypass
	doc.db_update_all()
	# ruleid: database-in-repositories, validation-bypass
	doc.update_child_table("entries")
	# ruleid: database-in-repositories, validation-bypass
	doc.update_children()
	# ruleid: database-in-repositories, validation-bypass
	doc.update_single({"rounding": 15})
	# ruleid: database-in-repositories, validation-bypass
	frappe.model.document.bulk_insert("NC Time Entry", entries)
	# ruleid: database-in-repositories, validation-bypass
	bulk_insert("NC Time Entry", entries)
	# ruleid: database-in-repositories, validation-bypass
	frappe.db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories, validation-bypass
	frappe.db.set_single_value("NC Settings", "rounding", 15)
	# ruleid: database-in-repositories, validation-bypass
	frappe.db.delete('NC Time Entry', {"name": name})
	# ruleid: database-in-repositories, validation-bypass
	frappe.db.truncate("NC Time Entry")
	# ruleid: database-in-repositories, validation-bypass
	frappe.db.bulk_insert("NC Time Entry", ["name"], [[name]])
	# ruleid: database-in-repositories, validation-bypass
	frappe.db.bulk_update("NC Time Entry", {name: {"minutes": 30}})
	# ruleid: database-in-repositories, validation-bypass
	frappe.db.delete(doctype="NC Time Entry")
	# ruleid: database-in-repositories, validation-bypass
	db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories, validation-bypass
	frappe.local.db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories, validation-bypass
	frappe.local.primary_db.set_value("NC Time Entry", name, "minutes", 30)
	# ruleid: database-in-repositories, validation-bypass
	frappe.local.replica_db.set_value("NC Time Entry", name, "minutes", 30)


def writes_with_the_query_builder(table, name, query, values, rows):
	# ruleid: database-in-repositories, validation-bypass
	frappe.qb.update(table).set(table.minutes, 0).run()
	# ruleid: database-in-repositories, validation-bypass
	built_for_later = frappe.qb.update(table).set(table.minutes, 0)
	# ruleid: database-in-repositories, validation-bypass
	frappe.qb.into(table).insert(name, 30).run()
	# ruleid: database-in-repositories, validation-bypass
	frappe.qb.from_(table).where(table.name == name).delete().run()
	# ruleid: database-in-repositories, validation-bypass
	deleted_later = frappe.qb.from_(table).where(table.name == name).delete()
	# ruleid: database-in-repositories, validation-bypass
	frappe.qb.get_query("NC Time Entry", delete=True, filters={"name": name})
	# ruleid: database-in-repositories, validation-bypass
	frappe.get_query("NC Time Entry", update=True)
	# ruleid: database-in-repositories, validation-bypass
	frappe.qb.get_query("NC Time Entry", into=True)
	# ruleid: validation-bypass
	table.update().set(table.minutes, 0).where(table.name == name).run()
	# ruleid: database-in-repositories, validation-bypass
	query.delete().run()

	# ok: validation-bypass
	values.update({"minutes": 30})


def deletes_and_renames_with_force(doc, name):
	# ruleid: database-in-repositories, validation-bypass
	frappe.delete_doc("NC Time Entry", name, force=True)
	# ruleid: database-in-repositories, validation-bypass
	frappe.delete_doc_if_exists("NC Time Entry", name, force=1)
	# ruleid: database-in-repositories, validation-bypass
	frappe.model.delete_doc.delete_doc("NC Time Entry", name, force=name)
	# ruleid: database-in-repositories, validation-bypass
	frappe.delete_doc("NC Time Entry", name, True)
	# ruleid: database-in-repositories, validation-bypass
	frappe.delete_doc_if_exists("NC Time Entry", name, True)
	# ruleid: database-in-repositories, validation-bypass
	doc.delete(force=True)
	# ruleid: database-in-repositories, validation-bypass
	frappe.rename_doc("NC Time Entry", name, "x", force=True)
	# ruleid: database-in-repositories, validation-bypass
	frappe.rename_doc("NC Time Entry", name, "x", True)
	# ruleid: validation-bypass
	doc.rename("x", force=True)
	# ruleid: validation-bypass
	doc.rename("x", False, True)
	# ruleid: validation-bypass
	doc._rename("x", False, True)

	# ruleid: database-in-repositories
	frappe.delete_doc("NC Time Entry", name, ignore_missing=False)
	# ruleid: database-in-repositories
	frappe.reload_doc("nc_times", "doctype", "nc_time_entry", force=True)
	# ruleid: database-in-repositories
	frappe.client.rename_doc("NC Time Entry", name, "x", True)


def erpnext_tables(name, doctype, values, own, table):
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.set_value("Sales Invoice", name, "status", "Paid")
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.set_single_value("Selling Settings", "so_required", "No")
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.delete("Timesheet", {"name": name})
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.truncate("Timesheet")
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.bulk_insert("Project", ["name"], [[name]])
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.bulk_update("Project", {name: {"status": "Open"}})
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.delete(doctype)
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.delete(f"NC {doctype}")
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.delete("NC Time Entry" if own else doctype)
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.set_value(dt="Sales Invoice", dn=name, field="status", val="Paid")
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.delete(doctype="Timesheet")
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.db.set_value(*values)
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	db.delete("Timesheet", {"name": name})
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.local.db.delete("Timesheet", {"name": name})
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.local.primary_db.set_value("Sales Invoice", name, "status", "Paid")
	# ruleid: database-in-repositories, validation-bypass, erpnext-through-documents
	frappe.local.replica_db.delete(doctype)
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.sql("select name from `tabNC Time Entry`")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.sql_list("select name from `tabProject`")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.sql_ddl("alter table `tabProject` add column x int")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.multisql({"mariadb": "select 1"})
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.execute_query("select 1")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.local.primary_db.sql("select 1")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.add_index("NC Time Entry", ["project"])
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.add_unique("NC Time Entry", ["project"])
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.rename_column("NC Time Entry", "minutes", "duration")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.rename_table("NC Time Entry", "NC Booking")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.change_column_type("NC Time Entry", "minutes", "int")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.updatedb("NC Time Entry")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.create_sequence("NC Time Entry")
	# ruleid: database-in-repositories, erpnext-through-documents
	frappe.db.set_next_sequence_val("NC Time Entry", 1)

	# ruleid: database-in-repositories, validation-bypass
	frappe.qb.update(frappe.qb.DocType("Sales Invoice")).set("status", "Paid")
	# ruleid: database-in-repositories, validation-bypass
	frappe.get_doc("Sales Invoice", name).db_set("status", "Paid")
	# ruleid: database-in-repositories
	frappe.db.get_value("Sales Invoice", name, "status")
	# ok: erpnext-through-documents
	frappe.cache.set_value("Sales Invoice", name)


def rollbacks(handle):
	# ruleid: database-in-repositories, manual-rollback
	frappe.db.rollback(save_point="before_booking")
	# ruleid: manual-rollback
	handle.rollback()
	# ruleid: manual-rollback
	with savepoint(catch=frappe.DuplicateEntryError):
		pass
	# ruleid: manual-rollback
	with rolls_back():
		pass

	# ruleid: database-in-repositories
	frappe.db.savepoint("before_booking")


# ruleid: manual-rollback
@savepoint(catch=Exception)
def rolls_back_when_it_fails(doc):
	pass


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


# ruleid: endpoint-checks-permission, endpoints-in-api, endpoint-names-methods
@frappe.whitelist()
def unchecked(entry: str):
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
@whitelist(methods=["POST"])
def unchecked_and_imported(entry: str):
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api, endpoint-names-methods
@frappe.whitelist()
def unchecked_with_a_parameter_named_self(self, entry: str):
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_without_throw(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry)
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_too_late(entry: str):
	entry = entry.strip()
	frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_in_a_branch(entry: str):
	if entry:
		frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_a_named_user(entry: str):
	frappe.has_permission("NC Time Entry", "write", entry, user="Administrator", throw=True)
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_a_user_by_position(entry: str):
	"""Preview the entry."""
	frappe.has_permission("NC Time Entry", "write", entry, "Administrator", throw=True)
	return entry


def plain(entry: str):
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api, endpoint-names-methods
whitelisted_by_call = frappe.whitelist()(plain)
# ruleid: endpoint-checks-permission, endpoints-in-api
kept_for_later = frappe.whitelist(methods=["POST"])


@kept_for_later
def whitelisted_by_a_variable(entry: str):
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api, endpoint-names-methods
kept_without_a_call = frappe.whitelist


# ruleid: endpoint-checks-permission, endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_only_if_given(entry: str):
	entry and frappe.has_permission("NC Time Entry", "write", entry, throw=True)
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
@frappe.whitelist(methods=["POST"])
def checks_only_if_empty(entry: str):
	entry or frappe.has_permission("NC Time Entry", "write", throw=True)
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
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
	# ok: endpoint-checks-permission, endpoints-in-api
	@frappe.whitelist(methods=["GET"])
	def preview(self):
		return self.minutes


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


# ruleid: endpoint-checks-permission, endpoints-in-api, endpoint-names-methods
@frappe.whitelist(allow_guest=True)
def names_no_method(entry: str):
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api, endpoint-names-methods
@whitelist()
def names_no_method_and_imported(entry: str):
	return entry


# ruleid: endpoint-checks-permission
@frappe.read_only()
# ruleid: endpoints-in-api, endpoint-names-methods
@frappe.whitelist()
def names_no_method_below_a_second_decorator(entry: str):
	return entry


# ruleid: endpoint-checks-permission, endpoints-in-api
whitelisted_by_call_with_its_method = frappe.whitelist(methods=["POST"])(plain)

# ruleid: endpoint-checks-permission, endpoints-in-api, endpoint-names-methods
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
