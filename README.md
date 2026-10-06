# Financial Report Percentage

Adds a **percentage column** to the **Profit and Loss Statement** report, like the classic
ERPNext "Show Percentage" option.

- Filter `Show Percentage` (checkbox, checked by default) is added to the report.
- Every row is shown as a percentage of the **total income** of the same column
  (total income = 100%,00) - exactly like the old ERPNext statement.
- The column is added on the right side and is also included in Excel export and PDF print.

## Install

```bash
bench get-app https://github.com/callmevan1120/financial_report_percentage
bench --site <site> install-app financial_report_percentage
```

## How it works

| File | Purpose |
| --- | --- |
| `overrides/percentage.py` | Calculates the percentages and appends the `percentage` column |
| `overrides/query_report.py` | Overrides `frappe.desk.query_report.run` (result) and `.get_script` (filter) |
| `overrides/monkey.py` | Rebinds `frappe.desk.query_report.run` so internal callers (Excel export) get the column too |

The percentage is based on the `total` column of the report; for reports without a
total column (e.g. yearly or accumulated values) the last period column is used.

The denominator (100%) is:

1. the classic income section total (sum of the top level income rows), when no
   Report Template is selected, or
2. the first revenue section (`indent = 0`, account data row) when a
   **Report Template** is used - consistent with the margin calculations inside
   the standard templates.

If the denominator is missing or zero the column is not added at all.

## Notes

- Only the `Profit and Loss Statement` report is affected (`SUPPORTED_REPORTS`
  in `overrides/percentage.py`).
- The print format refuses reports with more than 8 visible columns; with the
  extra column a report with 8 period columns can no longer be printed.
- No JavaScript assets are shipped: the checkbox is injected server side via
  `frappe.desk.query_report.get_script`.

## License

mit
