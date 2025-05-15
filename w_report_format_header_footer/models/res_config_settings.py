# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def edit_external_header(self):
        """Handle editing of the report header template based on the selected layout"""
        if not self.external_report_layout_id:
            return False
            
        # Check if our layout is selected by matching the view_id
        layout = self.external_report_layout_id
        view = layout.view_id
        
        if view and view.xml_id and 'external_layout_distintec' in view.xml_id:
            return self._prepare_report_view_action('w_report_format_header_footer.external_layout_distintec')
            
        # Default behavior for other layouts
        return self._prepare_report_view_action(view.xml_id) if view and view.xml_id else False