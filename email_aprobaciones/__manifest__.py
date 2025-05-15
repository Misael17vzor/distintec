# -*- coding: utf-8 -*-
{
    'name': "Email Aprobaciones",
    'summary': """
        Send email in aprobaciones""",
    'description': """
        Send email in aprobaciones
    """,
    'author': "Quemari developers",
    'website': "http://www.quemari.com",
    'category': 'Approvals',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'depends': [
        'approvals'
    ],
    'data': [
        'data/email_autorizador_template.xml',
        'data/email_solicitador_template.xml',
        'views/approval_category_inherit.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}