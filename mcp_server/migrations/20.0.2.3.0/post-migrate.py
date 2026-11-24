"""Remove the database default that ``pre-migrate`` set on ``ir_ui_view.visibility``."""

from odoo.tools.sql import column_exists


def migrate(cr, version):
    if not version or not column_exists(cr, "ir_ui_view", "visibility"):
        return
    cr.execute("ALTER TABLE ir_ui_view ALTER COLUMN visibility DROP DEFAULT")
