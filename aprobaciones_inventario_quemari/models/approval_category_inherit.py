from odoo import fields, models, api, _

class ApprovalCategoryInherit(models.Model):
    _inherit = 'approval.category'

    stock_picking_type_id = fields.Many2one('stock.picking.type', string='Tipo de Operación', domain=[('code', 'in', ['outgoing', 'internal'])] )
    user_product = fields.Selection([
                                    ('required', 'Requerido'),
                                    ('optional', 'Opcional'),
                                    ('no', 'Ninguno')], string='Solicitado por', default='no')