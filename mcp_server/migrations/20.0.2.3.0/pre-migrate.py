"""Give ``ir_ui_view.visibility`` a database default while the module loads.

Since 20.0 the ``website`` module makes ``ir.ui.view.visibility`` required. The
module does not depend on ``website`` and loads before it, so the views that this
version adds are inserted without a value, and the NOT NULL constraint of the
column rejects them. The column gets the ORM default ``public`` as its database
default here; ``post-migrate`` removes it again after the data load.
"""

from odoo.tools.sql import column_exists


def migrate(cr, version):
    if not version or not column_exists(cr, "ir_ui_view", "visibility"):
        return
    cr.execute("ALTER TABLE ir_ui_view ALTER COLUMN visibility SET DEFAULT 'public'")
