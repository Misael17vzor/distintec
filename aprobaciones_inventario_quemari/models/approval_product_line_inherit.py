from odoo import fields, models, api, _

class ApprovalProductLineInherit(models.Model):
    _inherit = 'approval.product.line'

    location_id = fields.Many2one('stock.location', string='Ubicación Origen')
    user_id = fields.Many2one('res.users', string='Solicitado por')
    stock_available = fields.Integer(string='Stock Disponible')

    @api.onchange('warehouse_id')
    def onchange_warehouse_id(self):
        for line in self:
            location_id = line.approval_request_id.category_id.stock_picking_type_id.default_location_src_id.id
            line.location_id = location_id

    @api.onchange('product_id', 'location_id', 'stock_available')
    def _onchange_stock_available(self):
        for record in self:
            quant_obj = self.env['stock.quant']
            quants = quant_obj.search([('product_id', '=', record.product_id.id), ('location_id', '=', record.location_id.id)])
            qty = sum([q.quantity for q in quants])
            record.stock_available = qty
