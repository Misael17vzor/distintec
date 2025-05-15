# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution

# Developer(s): Luis Ernesto García Medina
#               (ernesto.r.2.em@gmail.com)
########################################################################

from odoo import fields, api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    initial_ipc = fields.Float(string="Initial IPC")