# Copyright (c) 2013, github and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Member')

class TestMember(unittest.TestCase):
	pass
