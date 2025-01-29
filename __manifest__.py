# -*- coding: utf-8 -*-
{
    'name': "Recibo",
    'summary': "Reporte para impresora térmica",
    'description': "Módulo para generar un reporte de factura en formato para impresora térmica.",
    'author': "",
    'website': "",
    'category': 'Reporting',
    'version': '1.0',
    'depends': ['account'],
    'data': [
        'reports/report_ticket.xml',
        "views/account_journal_view.xml",
        "views/account_move_view.xml"
    ],
}
