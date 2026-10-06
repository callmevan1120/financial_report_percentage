app_name = "financial_report_percentage"
app_title = "Financial Report Percentage"
app_publisher = "callmevan1120"
app_description = "Adds a percentage column to the Profit and Loss Statement report"
app_email = "callmevan1120@users.noreply.github.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "financial_report_percentage",
# 		"logo": "/assets/financial_report_percentage/logo.png",
# 		"title": "Financial Report Percentage",
# 		"route": "/financial_report_percentage",
# 		"has_permission": "financial_report_percentage.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/financial_report_percentage/css/financial_report_percentage.css"
# app_include_js = "/assets/financial_report_percentage/js/financial_report_percentage.js"

# include js, css files in header of web template
# web_include_css = "/assets/financial_report_percentage/css/financial_report_percentage.css"
# web_include_js = "/assets/financial_report_percentage/js/financial_report_percentage.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "financial_report_percentage/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "financial_report_percentage/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "financial_report_percentage.utils.jinja_methods",
# 	"filters": "financial_report_percentage.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "financial_report_percentage.install.before_install"
# after_install = "financial_report_percentage.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "financial_report_percentage.uninstall.before_uninstall"
# after_uninstall = "financial_report_percentage.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "financial_report_percentage.utils.before_app_install"
# after_app_install = "financial_report_percentage.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "financial_report_percentage.utils.before_app_uninstall"
# after_app_uninstall = "financial_report_percentage.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "financial_report_percentage.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "financial_report_percentage.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["financial_report_percentage.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"financial_report_percentage.tasks.all"
# 	],
# 	"daily": [
# 		"financial_report_percentage.tasks.daily"
# 	],
# 	"hourly": [
# 		"financial_report_percentage.tasks.hourly"
# 	],
# 	"weekly": [
# 		"financial_report_percentage.tasks.weekly"
# 	],
# 	"monthly": [
# 		"financial_report_percentage.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "financial_report_percentage.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "financial_report_percentage.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
override_whitelisted_methods = {
	"frappe.desk.query_report.run": "financial_report_percentage.overrides.query_report.run",
	"frappe.desk.query_report.get_script": "financial_report_percentage.overrides.query_report.get_script",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "financial_report_percentage.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
before_request = ["financial_report_percentage.overrides.monkey.patch"]
# after_request = ["financial_report_percentage.utils.after_request"]

# Job Events
# ----------
before_job = ["financial_report_percentage.overrides.monkey.patch"]
# after_job = ["financial_report_percentage.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"financial_report_percentage.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

