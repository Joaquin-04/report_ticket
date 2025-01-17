# -*- coding: utf-8 -*-
{
    'name': "report_ticket_template",
    'summary': "Reporte para impresora térmica",
    'description': "Módulo para generar un reporte de factura en formato para impresora térmica.",
    'author': "OutsourceArg",
    'website': "https://www.outsourcearg.com",
    'category': 'Reporting',
    'version': '1.0',
    'depends': ['account'],
    'data': [
        'reports/report_ticket.xml',
        'reports/report_header.xml',
        'reports/report_footer.xml',
    ],
}
