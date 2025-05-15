{
    'name': 'Prevent Duplicated Sales',
    'version': '17.0',
    'summary': """Prevents duplicated sales orders""",
    'description': """
        This module prevents the creation of duplicated sales orders based on
        specific criteria.
    """,
    'author': '',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base', 'sale_management',
    ],
    'data': [
        'views/sale_order.xml',
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        
    }
}