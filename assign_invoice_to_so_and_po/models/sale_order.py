# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def show_sale_order_invoice_assigment(self):
        return {
            'view_mode' : 'form',
            'type': 'ir.actions.act_window',
            'res_model' : 'assign.invoice.to.so.and.po.wizard',
            'target' : 'new',
            'view_id' : self.env.ref('assign_invoice_to_so_and_po.assign_invoice_to_so_and_po_view_form').id,
        }