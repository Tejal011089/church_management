from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "First Timer",
					"description": _("First Timer"),
				},
				{
					"type": "doctype",
					"name": "Member",
					"description": _("Member Details"),
				},
			]
		},
		{
			"label": _("Main Reports"),
			"icon": "icon-table",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customer Acquisition and Loyalty",
					"doctype": "Customer",
					"label":"Member Details",
					"icon": "icon-bar-chart",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Lead Details",
					"doctype": "Lead",
					"label":"First Timer Details"
				},
			]
		},
	]
