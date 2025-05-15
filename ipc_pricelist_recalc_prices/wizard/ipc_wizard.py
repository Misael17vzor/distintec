# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution

# Developer(s): Luis Ernesto García Medina
#               (ernesto.r.2.em@gmail.com)
########################################################################

from odoo import fields, api, models, _

from odoo.exceptions import ValidationError

class PricelistIpcWizard(models.TransientModel):

    _name = 'pricelist.ipc.wizard'
    _description = 'Wizard to update prices based on IPC'

    current_ipc = fields.Float()

    
    def update_prices_ipc(self):
        self.ensure_one()
        ProductPricelist = self.env['product.pricelist']
        active_id = self.env.context.get('active_id')
        pricelist_id = ProductPricelist.browse(active_id)
        if not pricelist_id.partner_id:
            raise ValidationError(_("Please, set a partner for this pricelist."))
        not_have_ipc = [history.last_ipc for history in pricelist_id.history_ipc_ids]
        last_ipc = 0
        if not not_have_ipc:
            if not pricelist_id.partner_id.initial_ipc:
                raise ValidationError(_("Please, set a initial ipc for the partner of this pricelist."))
            last_ipc = pricelist_id.partner_id.initial_ipc
        else:
            last_ipc_id = pricelist_id.history_ipc_ids.sorted(key=lambda r: r.create_date, reverse=True)[0]
            last_ipc = last_ipc_id.last_ipc
        percent_adju = (self.current_ipc/last_ipc) - 1

        #Realizar registro de historico
        ipc_his_vals = []
        for item in pricelist_id.item_ids:
            if item.applied_on in ('1_product', '0_product_variant') and item.compute_price == 'fixed':
                dict_data = {'pricelist_id': active_id,
                     'product_id': item.product_id.id if item.product_id else False,
                     'before_price': item.fixed_price,
                     'new_price': item.fixed_price + (item.fixed_price * percent_adju),
                     'current_ipc': last_ipc,
                     'percent': percent_adju,
                     'last_ipc': self.current_ipc,
                     'increase': item.fixed_price * percent_adju}
                if item.applied_on == '1_product':
                    dict_data['product_tmpl_id'] = item.product_tmpl_id.id
                elif item.applied_on == '0_product_variant':
                    dict_data['product_id'] = item.product_id.id
                ipc_his_vals.append(dict_data)
                item.write({'fixed_price': item.fixed_price + (item.fixed_price * percent_adju)})
        if ipc_his_vals:
            self.env['pricelist.history.ipc'].create(ipc_his_vals)
        return True