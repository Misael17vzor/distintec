# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
#
########################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################

{
    'name': 'No Duplicated Sales',
    'author': 'QUEMARI ©',
    'category': 'Extra Tools',
    'sequence': 50,
    'summary': 'No Duplicated Sale Orders.',
    'website': 'https://www.quemari.com',
    'version': '1.0',
    'description': """
No Duplicated Sales
===========================

For DISTINTEC company, no duplicated Sales orders

Features
--------

* New constraint type: unique, field(s): partner_id & client_order_ref.

License
-------

GNU General Public License as published by the Free Software Foundation, version 3
<https://www.gnu.org/licenses/gpl-3.0.en.html>
        """,
    'depends': [
        'sale',
        'sale_management'
    ],
    'data': [
        'views/inherited_sale_views.xml',
    ],
    'demo': [],
    'qweb': [],
    'application': False,
    'installable': False,
}
