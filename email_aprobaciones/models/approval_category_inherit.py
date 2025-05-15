from odoo import fields, models, api, _

class ApprovalCategory(models.Model):
    _inherit = 'approval.category'

    users_cc_email_pending = fields.Many2many('res.users', relation='approval_pending_res_user', string="Notificar en estatus Enviado a")
    users_cc_email_approved = fields.Many2many('res.users', relation='approval_approved_res_user', string="Notificar en estatus Aprobado ")
    users_cc_email_refused = fields.Many2many('res.users', relation='approval_refused_res_user', string="Notificar en estatus Rechazado a")