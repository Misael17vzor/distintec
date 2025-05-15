# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AssignInvoiceToSo(models.TransientModel):
    _name='assign.invoice.to.so.and.po.wizard'
    
    def _custom_domain_invoice_ids(self):
        model = self._context.get('active_model')
        if model == 'sale.order':
            return [('move_type', 'in', ['out_invoice', 'out_refund'])]
        if model == 'purchase.order':
            return [('move_type', 'in', ['in_invoice', 'in_refund'])]
    
    is_unlink = fields.Boolean(string='Desvincular facturas seleccionadas', default=False)
    invoice_ids = fields.Many2many('account.move', string='Facturas a relacionar', domain=_custom_domain_invoice_ids)

    def assign_invoice_confirm(self):
        model = self._context.get('active_model')
        if self.is_unlink:
            if model == 'sale.order':
                so_id = self._context.get('active_id', False)
                so = self.env['sale.order'].search([('id', '=', so_id)])
                for invoice in self.invoice_ids:
                    so.order_line.write({'invoice_lines' : [(3, invoice.invoice_line_ids[0].id)] })
            if model == 'purchase.order':
                po_id = self._context.get('active_id', False)
                po = self.env['purchase.order'].search([('id', '=', po_id)])
                for invoice in self.invoice_ids:
                    po.order_line.write({'invoice_lines' : [(3, invoice.invoice_line_ids[0].id)] })
        else:
            if model == 'sale.order':
                so_id = self._context.get('active_id', False)
                so = self.env['sale.order'].search([('id', '=', so_id)])
                for invoice in self.invoice_ids:
                    so.order_line.write({'invoice_lines' : [(4, invoice.invoice_line_ids[0].id)] })
            if model == 'purchase.order':
                po_id = self._context.get('active_id', False)
                po = self.env['purchase.order'].search([('id', '=', po_id)])
                purchase_order_line_ids = po.order_line.mapped('id')
                stock_move_obj = self.env['stock.move']
                picking_ids = stock_move_obj.search([('purchase_line_id', 'in', purchase_order_line_ids)]).mapped('picking_id')
                for picking in picking_ids:
                    for invoice in self.invoice_ids:
                        picking.write({'invoice_ids' : [(4, invoice.id)]})
                for invoice in self.invoice_ids:
                    po.order_line.write({'invoice_lines' : [(4, invoice.invoice_line_ids[0].id)] })
                    for picking in picking_ids:
                        invoice.write({'picking_ids' : [(4, picking.id)]})
   