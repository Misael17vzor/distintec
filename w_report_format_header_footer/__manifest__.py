# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
#
# Developer(s): Luis Ernesto García Medina
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
    'name': 'Header and footer format for Distintec',
    'author': 'QUEMARI ©',
    'category': 'Extra Tools',
    'summary': 'Header and footer format for Distintec.',
    'website': 'https://www.quemari.com',
    'version': '17.0.1.0',  # Updated version for Odoo 17
    'description': """
Header and footer format for Distintec
==============================================


License
=======

GNU General Public License as published by the Free Software Foundation, version 3
<https://www.gnu.org/licenses/gpl-3.0.en.html>

        """,
    'depends': [
        'web',
        'base',
        'sale',         # Added for sale order reports
        'purchase',     # Added for purchase order reports
        'stock',        # Added for stock picking/move reports
        'quality',      # Added for quality certificate reports (if using the quality module)
    ],
    'data': [
        'views/report_template.xml',  # First load the template
        'data/report_layout.xml',     # Then register it in report.layout
    ],
    'assets': {
        'web.report_assets_common': [
            '/w_report_format_header_footer/static/src/scss/layout_distintec.scss',
        ],
        'web.report_assets_pdf': [
            '/w_report_format_header_footer/static/src/scss/layout_distintec.scss',
        ],
        'web.report_assets': [
            '/w_report_format_header_footer/static/src/scss/layout_distintec.scss',
        ],
    },
    'demo': [],
    'images': [
        'static/img/preview_standard.png',
    ],
    'application': False,
    'installable': True,
    'license': 'GPL-3',
}

