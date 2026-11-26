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
