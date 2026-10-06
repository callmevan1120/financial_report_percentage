"""Overrides for `frappe.desk.query_report`.

- `run` adds the percentage column to the report result.
- `get_script` injects the `Show Percentage` filter into the report's JS.
"""

import frappe
from frappe.desk import query_report as _query_report

from financial_report_percentage.overrides import percentage

# captured at import time, before monkey.py patches the module (see monkey.py)
_original_run = _query_report.run
_original_get_script = _query_report.get_script

SHOW_PERCENTAGE_FILTER_JS = """
// injected by financial_report_percentage
(function () {
	const report_name = "Profit and Loss Statement";
	const settings = frappe.query_reports && frappe.query_reports[report_name];
	if (!settings) return;

	settings.filters = settings.filters || [];
	if (!settings.filters.some((filter) => filter.fieldname === "show_percentage")) {
		settings.filters.push({
			fieldname: "show_percentage",
			label: __("Show Percentage"),
			fieldtype: "Check",
			default: 1,
		});
	}
})();
"""


@frappe.whitelist()
@frappe.read_only()
def run(*args, **kwargs):
	response = _original_run(*args, **kwargs)

	report_name = kwargs.get("report_name") or (args[0] if args else None)
	if report_name not in percentage.SUPPORTED_REPORTS:
		return response

	filters = kwargs.get("filters")
	if filters is None and len(args) > 1:
		filters = args[1]

	if not percentage.is_enabled(filters):
		return response

	return percentage.add_percentage_column(response)


@frappe.whitelist()
@frappe.read_only()
def get_script(report_name):
	response = _original_get_script(report_name)
	if report_name in percentage.SUPPORTED_REPORTS and isinstance(response, dict):
		response["script"] = (response.get("script") or "") + SHOW_PERCENTAGE_FILTER_JS
	return response
