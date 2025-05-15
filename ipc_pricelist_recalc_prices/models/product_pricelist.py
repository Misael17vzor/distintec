# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution

# Developer(s): Luis Ernesto García Medina
#               (ernesto.r.2.em@gmail.com)
########################################################################

from odoo import fields, api, models, _


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    history_ipc_ids = fields.One2many('pricelist.history.ipc', 'pricelist_id')
    partner_id = fields.Many2one('res.partner')

    
    def open_ipc_pricelist_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Update prices - IPC'),
            'res_model': 'pricelist.ipc.wizard',
            'view_mode': 'form',
            'target': 'new',
        }


class PricelistHistoryIpc(models.Model):
    _name = "pricelist.history.ipc"
    _description = "Pricelist History IPC"

    pricelist_id = fields.Many2one('product.pricelist')
    product_id = fields.Many2one('product.product')
    product_tmpl_id = fields.Many2one('product.template')
    before_price = fields.Float()
    new_price = fields.Float()
    current_ipc = fields.Float()
    percent = fields.Float()
    last_ipc = fields.Float()
    increase = fields.Float()