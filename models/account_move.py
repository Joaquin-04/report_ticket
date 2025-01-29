from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    letra_factura = fields.Char(
        string="Letra Factura",
        compute="_compute_letra_factura",
        store=True
    )

    @api.depends("name")
    def _compute_letra_factura(self):
        for record in self:
            letra = str(record.name.split(" ")[0]) if record.name else ""
            if letra and letra != "/":
                record.letra_factura = letra[3:4]
            else:
                record.letra_factura = ""