# Copyright (c) 2013, github and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Member(Document):
	pass

	#To create customer in ERP when we create member in Church Management App
	def on_update(self):
		#frappe.errprint("in on update")
		check_customer=frappe.db.sql(""" select name from `tabCustomer` where member_id='%s'"""%self.name,as_list=1,debug=1)
		if check_customer:
			pass
		else:
			self.create_customer()


	#Create customer when we create member in App
	def create_customer(self):
		#frappe.errprint("in create customer")
		customer = frappe.new_doc("Customer")
		customer.customer_name=self.customer_name
		customer.customer_type=self.customer_type
		customer.lead_name=self.lead_name
		customer.customer_group=self.customer_group
		customer.territory=self.territory
		customer.company=self.company
		customer.customer_details=self.customer_details
		customer.default_currency=self.default_currency
		customer.default_price_list=self.default_price_list
		customer.default_taxes_and_charges=self.default_taxes_and_charges
		customer.credit_days=self.credit_days
		customer.credit_limit=self.credit_limit
		customer.website=self.website
		customer.member_id=self.name
		customer.save()
		