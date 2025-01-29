from odoo import models, fields

class AccountJournal(models.Model):
    _inherit = "account.journal"

    direccion = fields.Text(
        string="Dirección",
        help="Dirección que saldrá en el recibo"
    )