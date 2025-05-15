from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

class ApprovalRequest(models.Model):
    _inherit='approval.request'

    user_id_options = fields.Boolean(string='Opciones aprobado por', compute='compute_id_options')

    @api.model
    @api.depends('category_id.user_product')
    def compute_id_options(self):
        for record in self:
            user_id_options = record.category_id.user_product
            if user_id_options == 'no':
                record.user_id_options = False
            if user_id_options == 'required':
                record.user_id_options = True

    # def action_confirm(self):
    #     for record in self:
    #         if record.product_line_ids:
    #             for line in record.product_line_ids:
    #                 if line.stock_available < line.quantity:
    #                     raise ValidationError('Las cantidades solicitadas del producto {} sobrepasan la cantidad de stock en la ubicación {}. No se puede enviar la solicitud.'.format(line.product_id.name, line.location_id.complete_name))
    #         return super(ApprovalRequest, self).action_confirm()

    def action_approve(self, approver=None):
        for record in self:
            if record.product_line_ids:
                for line in record.product_line_ids:
                    if line.stock_available < line.quantity:
                        raise ValidationError('Las cantidades solicitadas del producto {} sobrepasan la cantidad de stock en la ubicación {}. No se puede aprobar la solicitud.'.format(line.product_id.name, line.location_id.complete_name))
            return super(ApprovalRequest, self).action_approve()