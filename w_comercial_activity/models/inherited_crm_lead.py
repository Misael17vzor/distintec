# -*- coding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2018-2025 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Sergio Ernesto Tostado Sánchez
#               (sergio.tostado@telematel.com)
#
########################################################################
import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class CrmTeam(models.Model):
    _inherit = 'crm.team'
    
    assign_user_id = fields.Many2one(
        "res.users", 
        string="User to Assign", 
        help="User to whom the customer will be assigned after the inactivity period"
    )


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def _cron_check_leads_comercial_activity_limit(self):
        mail_activity_obj = self.env['mail.activity']
        # Search all neither won nor lost leads
        open_leads = self.search([
            '|',
            '&',
            ('probability', '!=', 100.0),
            ('active', '=', True),
            '&',
            ('probability', '=', 0.0),
            ('active', '=', True)
        ])
        
        meeting_activity_type = self.env.ref('mail.mail_activity_data_meeting', raise_if_not_found=False)
        if not meeting_activity_type:
            _logger.error(_("Meeting activity type not found"))
            return
            
        for lead in open_leads:
            customer = lead.partner_id
            salesperson = customer.user_id
            sales_channel = customer.team_id
            
            if customer and salesperson and sales_channel:
                activities = mail_activity_obj.search([
                    ('res_model', '=', 'crm.lead'),
                    ('res_id', '=', lead.id),
                    ('activity_type_id', '=', meeting_activity_type.id)
                ])
                
                if activities:
                    for activity in activities:
                        overdue_days = activity._compute_number_overdue_days()
                        
                        if (overdue_days >= customer.no_comercial_act_limit and 
                            sales_channel.user_id and 
                            sales_channel.user_id.id != salesperson.id and
                            sales_channel.assign_user_id):
                            
                            _logger.warning(_(
                                '%(lead)s: Found an activity with %(days)s day(s) of %(limit)s available for customer %(customer)s, '
                                'scaling to %(team)s\'s Team Leader ...'
                            ) % {
                                'lead': lead.name,
                                'days': overdue_days,
                                'limit': customer.no_comercial_act_limit,
                                'customer': customer.name,
                                'team': sales_channel.name
                            })
                            
                            lead.write({'user_id': sales_channel.user_id.id})
                            lead.partner_id.write({'user_id': sales_channel.assign_user_id.id})
                            
                            _logger.info(_("Changed %(old)s salesperson to %(new)s.") % {
                                'old': salesperson.name,
                                'new': sales_channel.user_id.name
                            })
                            break
                else:
                    _logger.info(_(
                        '%(lead)s doesn\'t have any scheduled activity and/or the sales channel leader '
                        'is the current salesperson, skipping ...'
                    ) % {'lead': lead.name})
            else:
                _logger.error(_(
                    '%(lead)s doesn\'t have any of these fields set: Customer (%(customer)s), '
                    'Salesperson (%(salesperson)s) or Sales Channel (%(channel)s). '
                    'Please set them to change Salesperson in next ir.cron run.'
                ) % {
                    'lead': lead.name,
                    'customer': customer.name if customer else _('missing'),
                    'salesperson': salesperson.name if salesperson else _('missing'),
                    'channel': sales_channel.name if sales_channel else _('missing')
                })