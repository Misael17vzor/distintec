# -*- coding_ utf-8 -*-

from odoo import fields, api, models, _
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class ApprovalInherit(models.Model):
    _inherit = 'approval.request'

    def action_confirm(self):
        if len(self.approver_ids) < self.approval_minimum:
            raise UserError(_("You have to add at least %s approvers to confirm your request.", self.approval_minimum))
        if self.requirer_document == 'required' and not self.attachment_number:
            raise UserError(_("You have to attach at lease one document."))
        approvers = self.mapped('approver_ids').filtered(lambda approver: approver.status == 'new')
        approvers.write({'status': 'pending'})
        approver_emails_list = []
        for approver in self.approver_ids:
            approver_emails_list.append(approver.user_id.email)
        approver_emails_str =','.join(approver_emails_list)
        mail_template = self.env.ref('email_aprobaciones.q_mail_template__autorizador_aprobaciones')
        emails_cc_list = []
        if self.category_id.users_cc_email_pending:
            for users_cc in self.category_id.users_cc_email_pending:
                emails_cc_list.append(users_cc.email)
        emails_cc_str = ','.join(emails_cc_list)
        if self.amount and self.amount >= 2000000:
            emails_cc_str += ',njelincic@distintec.cl,sajelincic@distintec.cl'
        mail_template.write({'email_to': approver_emails_str, 'email_cc': emails_cc_str})
        mail_template.send_mail(self.id, force_send = True)
        self.write({'date_confirmed': fields.Datetime.now()})
        return super(ApprovalInherit, self).action_confirm()

    def action_approve(self, approver=None):
        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        approver.write({'status': 'approved'})
        mail_template = self.env.ref('email_aprobaciones.q_mail_template_solicitador_aprobaciones')
        emails_cc_list = []
        if self.category_id.users_cc_email_approved:
            for users_cc in self.category_id.users_cc_email_approved:
                emails_cc_list.append(users_cc.email)
        emails_cc_str = ','.join(emails_cc_list)
        mail_template.write({'email_to': self.request_owner_id.email, 'email_cc': emails_cc_str})
        mail_template.send_mail(self.id, force_send = True)
        self.sudo()._get_user_approval_activities(user=self.env.user).action_feedback()
        return super(ApprovalInherit, self).action_approve()

    def action_refuse(self, approver=None):
        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        approver.write({'status': 'refused'})
        mail_template = self.env.ref('email_aprobaciones.q_mail_template_solicitador_aprobaciones')
        emails_cc_list = []
        if self.category_id.users_cc_email_refused:
            for users_cc in self.category_id.users_cc_email_refused:
                emails_cc_list.append(users_cc.email)
        emails_cc_str = ','.join(emails_cc_list)
        mail_template.write({'email_to': self.request_owner_id.email, 'email_cc': emails_cc_str})
        mail_template.send_mail(self.id, force_send = True)
        self.sudo()._get_user_approval_activities(user=self.env.user).action_feedback()
        return super(ApprovalInherit, self).action_refuse()

    def action_withdraw(self, approver=None):
        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        approver.write({'status': 'pending'})
        mail_template = self.env.ref('email_aprobaciones.q_mail_template_solicitador_aprobaciones')
        emails_cc_list = []
        if self.category_id.users_cc_email_pending:
            for users_cc in self.category_id.users_cc_email_pending:
                emails_cc_list.append(users_cc.email)
        emails_cc_str = ','.join(emails_cc_list)
        mail_template.write({'email_to': self.request_owner_id.email, 'email_cc': emails_cc_str})
        mail_template.send_mail(self.id, force_send = True)
        self.sudo()._get_user_approval_activities(user=self.env.user).action_feedback()
        return super(ApprovalInherit, self).action_withdraw()