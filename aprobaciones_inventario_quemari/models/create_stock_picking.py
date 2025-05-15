from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import logging
logger = logging.getLogger('$$$$$$$$$$$$$$$$$$$')

class CreateStockPicking(models.Model):
    _inherit = 'approval.request'

    stock_picking_id = fields.Many2one('stock.picking', string='Transferencia de Inventario')

    def action_approve(self, approver=None):
        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        approver.write({'status': 'approved'})
        if self.request_status == 'approved' and self.product_line_ids:
            if not self.category_id.stock_picking_type_id.default_location_src_id or not self.category_id.stock_picking_type_id.default_location_dest_id:
                raise ValidationError('Es necesario que el Tipo de Operación relacionado cuente con ubicación de origen y destino. Contacte a su administrador del sistema.')
            stock_picking_obj = self.env['stock.picking']
            stock_picking_values = {
                'name' : '/',
                'picking_type_id' : self.category_id.stock_picking_type_id.id,
                'location_id' : self.category_id.stock_picking_type_id.default_location_src_id.id,
                'location_dest_id' : self.category_id.stock_picking_type_id.default_location_dest_id.id,
                'origin' : self.name
            }
            stock_picking = stock_picking_obj.sudo().with_context({'default_name' : '/'}).create(stock_picking_values)
            self.stock_picking_id = stock_picking

            for product_line in self.product_line_ids:
                stock_move_obj = self.env['stock.move']
                stock_move_vlues = {
                    'picking_id' : stock_picking.id,
                    'product_id' : product_line.product_id.id,
                    'name' : product_line.description,
                    'description_picking' : product_line.description,
                    'location_id' : product_line.location_id.id,
                    'location_dest_id' : stock_picking.location_dest_id.id,
                    'product_uom_qty' : product_line.quantity,
                    'product_uom' : product_line.product_uom_id.id
                }
                stock_moves = stock_move_obj.sudo().create(stock_move_vlues)
            stock_picking.action_confirm()

        self.sudo()._get_user_approval_activities(user=self.env.user).action_feedback()
        return super(CreateStockPicking, self).action_approve()

    def show_approval_picking(self):
        action = self.env["ir.actions.actions"]._for_xml_id("stock.action_picking_tree_all")
        action['views'] = [
            (self.env.ref('stock.vpicktree').id, 'tree'),
            (self.env.ref('stock.view_picking_form').id, 'form')
        ]
        action['context'] = self.env.context
        action['domain'] = [('id', '=', self.stock_picking_id.id)]
        logger.info(action)
        return action
