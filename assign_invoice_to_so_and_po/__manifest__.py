# -*- coding: utf-8 -*-
{
    'name': "Asignación de facturas a órdenes de venta y órdenes de compra",
    'summary': 'Asignación de facturas a órdenes de venta y órdenes de compra',
    'author': 'QUEMARI ©',
    'website': "http://www.quemari.com",
    'version': '17.0.1.0',  # Updated version for Odoo 17
    'category': 'Sales',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management',
        'purchase',
        'account',
        'stock',
    ],
    # always loaded
    'data': [
        # 'views/purchase_order.xml',
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'wizard/assign_invoice_to_so_and_po_wizard.xml',
        'views/groups_assign_invoice.xml',
        'views/account_move.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': False,
}
