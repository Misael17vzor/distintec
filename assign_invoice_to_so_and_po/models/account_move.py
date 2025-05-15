# -*- encoding: utf-8 -*_
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    picking_ids = fields.Many2many('stock.picking', string='Picking Relacionados')

    def show_related_picking_ids(self):
        action = self.env["ir.actions.actions"]._for_xml_id("stock.action_picking_tree_all")
        action['views'] = [
            (self.env.ref('stock.vpicktree').id, 'tree'),
            (self.env.ref('stock.view_picking_form').id, 'form')
        ]
        action['context'] = self.env.context
        action['domain'] = [('id', 'in', self.picking_ids.mapped('id'))]
        return action