# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2018 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Sergio Ernesto Tostado Sánchez
#               (sergio.tostado@telematel.com)
#
########################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    no_comercial_act_limit = fields.Integer(
        string="Limit for No Comercial Activity",
        default=10,
        help="Number of days that you set for no changes about \
              Comercial Lead activities (default=10 days)."
    )