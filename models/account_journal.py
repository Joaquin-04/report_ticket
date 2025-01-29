from odoo import models, fields

class AccountJournal(models.Model):
    _inherit = "account.journal"

    direccion = fields.Char(
        string="Dirección",
        help="Dirección que saldrá en el recibo"
    )