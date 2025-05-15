# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution

# Developer(s): Luis Ernesto García Medina
#               (ernesto.r.2.em@gmail.com)
########################################################################
{
    'name': 'DISTINTEC | IPC for pricelist by partner',
    'author': '@Neto_odoo',
    'category': 'Sales',
    'sequence': 50,
    'summary': "DISTINTEC | IPC for pricelist by partner",
    'website': 'http://www.twitter.com/neto_odoo',
    'version': '17.0.1.0',
    'description': """
IPC for pricelist by partner
        """,
    'depends': [
        'sale_management'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/product_pricelist_view.xml',
        'wizard/ipc_wizard_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}