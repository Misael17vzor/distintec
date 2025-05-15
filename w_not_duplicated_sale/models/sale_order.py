# -*- encoding: utf-8 -*-

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
        ('unique_commercial_po_sale', 'unique(commercial_partner_id, client_order_ref)', 
         'Venta Duplicada: La Orden de Compra ya ha sido usada para este Cliente,\n'
         'prueba establecer otra Orden de Compra o bien, cambiar de Cliente.')
    ]