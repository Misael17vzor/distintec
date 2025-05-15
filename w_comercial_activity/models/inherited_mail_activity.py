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

from datetime import date, datetime, timedelta
import pytz

from odoo import api, fields, models, _


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    def _compute_number_overdue_days(self):
        """Compute the number of days an activity is overdue.
        
        Returns:
            int: Number of days the activity is overdue, or 0 if not overdue
        """
        self.ensure_one()
        today = date.today()
        
        # Consider user's timezone if available
        tz = self.env.user.sudo().tz
        if tz:
            today_utc = pytz.UTC.localize(datetime.utcnow())
            today_tz = today_utc.astimezone(pytz.timezone(tz))
            today = date(year=today_tz.year, month=today_tz.month, day=today_tz.day)
            
        date_deadline = self.date_deadline
        diff = (date_deadline - today)
        
        # Activity is state = overdue
        if diff.days < 0:
            return abs(diff.days)
        # Activity is for either today or planned
        else:
            return 0