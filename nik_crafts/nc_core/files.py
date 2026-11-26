"""A file's name keeps the type of the file stored under it."""

from mimetypes import guess_type

import frappe
from frappe import _


def keep_the_type(doc, _method):
	if doc.is_folder or doc.is_remote_file:
		return
	if guess_type(doc.file_name)[0] != guess_type(doc.file_url)[0]:
		frappe.throw(_("The name of a file must keep the type it was stored with."))
