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

import logging

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    
    _inherit = 'sale.order'

    commercial_partner_id = fields.Many2one('res.partner', string='Entidad Comercial')

    @api.onchange('partner_id')
    def _onchange_commercial_partner_id(self):
            commercial_res_partner = self.partner_id.commercial_partner_id.id
            self.commercial_partner_id = commercial_res_partner

    _sql_constraints = [
        ('unique_commercial_po_sale', 'unique(commercial_partner_id, client_order_ref)', 'Venta Duplicada: La Orden de Compra ya ha sido usada para este Cliente,\nprueba establecer otra Orden de Compra o bien, cambiar de Cliente.')
    ]
