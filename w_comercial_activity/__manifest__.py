# -*- coding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2018-2025 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Sergio Ernesto Tostado Sánchez
#               (sergio.tostado@telematel.com)
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
    'name': 'TELEMATEL | Comercial\'s Activity Control',
    'author': 'TELEMATEL ©',
    'category': 'Customer Relationship Management',
    'sequence': 50,
    'summary': "TELEMATEL Comercial\'s Activity Control for Distintec.",
    'website': 'https://www.telematel.com',
    'version': '17.0.1.0',
    'description': """
TELEMATEL | Comercial\'s Activity Control
=========================================

For DISTINTEC company, Comercial's activities in control.

Features
========

* ADD: Limit of No-Comercial activity (no_comercial_act_limit) field in partners.
* ADD: ir.cron to check number of days that you set for no-modification about Comercial Lead activities.

License
=======

GNU General Public License as published by the Free Software Foundation, version 3
<https://www.gnu.org/licenses/gpl-3.0.en.html>


Authors
=======

* Sergio Ernesto Tostado Sánchez (sergio.tostado@telematel.com)
        """,
    'depends': [
        'base',
        'base_automation',
        'crm',
        'mail'
    ],
    'data': [
        'security/security.xml',
        'data/ir_cron.xml',
        'views/inherited_res_partner_views.xml'
    ],
    'assets': {},
    'license': 'GPL-3',
    'application': False,
    'installable': True,
    'auto_install': False,
}