import frappe
import requests
from frappe import local as site
from frappe.core.doctype.user.user import impersonate
from frappe.model.delete_doc import delete_doc as remove
from frappe.model.rename_doc import rename_doc


def document_methods(doc, rows, pool, image, job, path, url, options):
	# ruleid: permission-bypass
	doc.delete(**options)

	# ok: permission-bypass
	rows.insert(0, doc)
	# ok: permission-bypass
	image.save("/tmp/file.png")
	# ok: permission-bypass
	requests.delete(url, options)
	# ok: permission-bypass
	options.delete("key", "other")


def permission_switches(doc, repository, name, flag, options, user):
	# ruleid: permission-bypass
	doc.insert(ignore_permissions=True)
	# ruleid: permission-bypass
	doc.save(ignore_permissions=flag)
	# ruleid: permission-bypass
	doc.delete(ignore_permissions=1)
	# ruleid: permission-bypass
	frappe.get_list(
		"NC Time Entry",
		filters={"name": name},
		ignore_permissions=True,
	)
	# ruleid: permission-bypass
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
	# ruleid: permission-bypass
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
	# ruleid: permission-bypass
	doc.insert(ignore_permissions=ignore_permissions)


def passes_the_switch_on_in_many_lines(
	doc,
	# ruleid: permission-bypass
	ignore_permissions: bool = False,
):
	return doc


def switches_by_position(doc, table, image, path, name, flag, args, options):
	# ruleid: permission-bypass
	doc.insert(flag)
	# ruleid: permission-bypass
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
	# ruleid: permission-bypass
	doc.save(**options)
	# ruleid: permission-bypass
	doc.delete(flag)
	# ruleid: permission-bypass
	doc.delete(False, True)
	# ruleid: permission-bypass
	image.save(path)
	# ruleid: permission-bypass
	frappe.delete_doc("NC Time Entry", name, 0, None, True)
	# ruleid: permission-bypass
	frappe.delete_doc("NC Time Entry", name, for_reload=True)
	# ruleid: permission-bypass
	frappe.delete_doc_if_exists("NC Time Entry", name, for_reload=True)
	# ruleid: permission-bypass
	remove("NC Time Entry", name, for_reload=True)
	# ruleid: permission-bypass
	rename_doc("NC Time Entry", name, "x", validate=False)
	# ruleid: permission-bypass
	doc.rename("x", validate_rename=False)
	# ruleid: permission-bypass
	doc._rename("x", validate_rename=False)
	# ruleid: permission-bypass
	rename_doc("NC Time Entry", name, "x", False, False, True)

	# ok: permission-bypass
	doc.insert(flag, True)
	# ok: permission-bypass
	frappe.cache.delete(name)


def acts_as_another_user(user, manager, reason):
	# ruleid: permission-bypass
	frappe.get_list("NC Time Entry", user=user)
	# ruleid: permission-bypass
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
