"""Adds a `percentage` column to financial statement reports.

A row's percentage is its value divided by the total income of the same
column/period (total income = 100%), matching the classic ERPNext
"Show Percentage" behaviour.
"""

import frappe
from frappe.utils import cint, flt

SUPPORTED_REPORTS = ("Profit and Loss Statement",)
PERCENTAGE_FIELDNAME = "percentage"
PERCENTAGE_LABEL = "%"

# Account types that must not count towards the gross income (100%), even when
# the accounts sit below the income root (e.g. cost of goods sold accounts).
COST_ACCOUNT_TYPES = frozenset(
	{
		"Cost of Goods Sold",
		"Expenses Included In Valuation",
		"Expenses Included In Asset Valuation",
		"Stock Adjustment",
		"Stock Received But Not Billed",
		"Depreciation",
		"Expense Account",
	}
)


def is_enabled(filters) -> bool:
	"""`show_percentage` defaults to 1 so the column is shown unless explicitly unchecked."""
	return bool(cint(as_dict(filters).get("show_percentage", 1)))


def as_dict(filters) -> dict:
	if not filters:
		return {}
	if isinstance(filters, str):
		filters = frappe.parse_json(filters) or {}
	return filters if isinstance(filters, dict) else {}


def get_value_fieldname(columns) -> str | None:
	"""Column the percentage is based on: `total` when present, else the last amount column."""
	fieldnames = [column.get("fieldname") for column in columns]
	if "total" in fieldnames:
		return "total"

	for column in reversed(columns):
		if column.get("fieldname") and column.get("fieldtype") in ("Currency", "Float"):
			return column["fieldname"]

	return None


def is_classic_total_row(row) -> bool:
	"""Total rows appended by `erpnext.accounts.report.financial_statements.add_total_row`."""
	return isinstance(row, dict) and bool(row) and "opening_balance" in row and "parent_account" not in row


def is_template_section_row(row) -> bool:
	"""First account data row (indent 0) of a report built with a Report Template."""
	return (
		isinstance(row, dict)
		and bool(row)
		and bool(row.get("account_filters"))
		and cint(row.get("indent")) == 0
		and not row.get("is_blank_line")
	)


def get_income_total(data, value_field) -> float | None:
	"""Total income for the column used as 100%."""
	rows = [row for row in data or [] if isinstance(row, dict) and row]
	if not rows:
		return None

	# report template engine: use the first revenue section
	if any(is_template_section_row(row) for row in rows):
		for row in rows:
			if is_template_section_row(row):
				return flt(row.get(value_field))
		return None

	# classic report: the income section ends where the first total row
	# (appended by `add_total_row`) starts
	income_rows = []
	for row in rows:
		if is_classic_total_row(row):
			break
		income_rows.append(row)

	return get_gross_income_total(income_rows, value_field)


def is_cost_account(row) -> bool:
	return (row.get("account_type") or "") in COST_ACCOUNT_TYPES


def get_gross_income_total(income_rows, value_field) -> float | None:
	"""Sum of the income accounts (leaves), leaving cost accounts out.

	Charts of accounts that nest the cost of goods sold below the income root
	make ERPNext's own total income a net figure (revenue minus costs), so the
	percentage has to be based on the gross income instead.
	"""
	found_leaf = False
	income_total = 0.0

	for row in income_rows:
		if row.get("is_group") or row.get("is_blank_line"):
			continue
		found_leaf = True
		if is_cost_account(row):
			continue
		income_total += flt(row.get(value_field))

	return income_total if found_leaf else None


def add_percentage_column(response: dict) -> dict:
	columns = response.get("columns") or []
	data = response.get("result") or []

	value_field = get_value_fieldname(columns)
	if not value_field:
		return response

	income_total = get_income_total(data, value_field)
	if not income_total:
		return response

	for row in data:
		if not isinstance(row, dict) or not row or row.get("is_blank_line"):
			continue
		row[PERCENTAGE_FIELDNAME] = flt(flt(row.get(value_field)) / income_total * 100, 2)

	if not any(column.get("fieldname") == PERCENTAGE_FIELDNAME for column in columns):
		columns.append(
			{
				"fieldname": PERCENTAGE_FIELDNAME,
				"label": PERCENTAGE_LABEL,
				"fieldtype": "Percent",
				"width": 120,
			}
		)

	return response
