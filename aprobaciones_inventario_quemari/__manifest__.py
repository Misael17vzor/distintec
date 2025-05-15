# -*- coding: utf-8 -*-
{
    "name": "Aprobaciones Inventario Quemari",
    "summary": "Afectación de inventario a través de aprobaciones",
    "license": "AGPL-3",
    "author": "Quemari developers",
    "website": "http://www.quemari.com",
    'version': '17.0.1.0',  # Updated version for Odoo 17
    "depends": [
        "approvals",
    ],
    "data": [
        "views/approval_product_line_inherit.xml",
        "views/approval_category_inherit_view.xml",
        "views/approval_request_inherit_view.xml",
    ],
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}
