# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
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

from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    # El campo estándar en Odoo es 'external_report_layout_id'.
    # Si tu intención es extender las opciones de ESE campo, asegúrate de que el nombre coincida.
    # Si 'external_report_layout_id' es el campo que quieres modificar (lo cual es lo más probable):
    external_report_layout_id = fields.Selection(
        selection_add=[('distintec', 'Distintec')],
        ondelete={'distintec': 'set default'} # O 'set null' o una función, según necesidad en Odoo 17+
    )
    # Si estabas creando un campo completamente nuevo con un nombre similar, entonces:
    # external_report_layout_id_custom = fields.Selection(selection_add=[
    #     ('distintec', 'Distintec'),
    # ], string='Document Template Custom')
    # Nota: El string original era 'Document Template', que es el string del campo estándar.
    # He mantenido 'external_report_layout_id' asumiendo que extiendes el campo estándar.