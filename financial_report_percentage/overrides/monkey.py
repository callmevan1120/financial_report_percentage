"""Patches `frappe.desk.query_report.run` so internal callers that import the
module level function (e.g. the Excel export in `_export_query`) also get the
percentage column.

The patch is idempotent and applied from the `before_request` hook.
"""

from frappe.desk import query_report as _query_report

_patched = False


def patch(**kwargs):
	global _patched
	if _patched:
		return

	from financial_report_percentage.overrides import query_report as overrides

	_query_report.run = overrides.run
	_patched = True
