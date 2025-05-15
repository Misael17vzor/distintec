# -*- coding: utf-8 -*-
{
    'name': 'Warehouse to CRM Teams',
    'version': '17.0.1.0.0',
    'summary': """Link warehouses with CRM sales teams""",
    'description': """
        This module allows linking warehouses with CRM sales teams,
        enabling better organization of warehouse operations based on sales teams.
    """,
    'license': 'LGPL-3',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Sales/CRM',
    'depends': ['base', 'sale_management', 'stock', 'crm'],
    "data": [
        "views/crm_team_views.xml"
    ],
    'images': [],
    'application': True,
    'installable': True,
    'auto_install': False,
}