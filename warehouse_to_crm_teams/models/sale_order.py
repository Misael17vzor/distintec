# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    @api.onchange('team_id')
    def onchange_team_id(self):
       self.warehouse_id = self.team_id.default_warehouse.id 