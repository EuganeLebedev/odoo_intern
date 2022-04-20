from odoo import models, fields, api
import json


class SaleOrderInherit(models.Model):

    _name = 'sale.order'
    _inherit = 'sale.order'

    exclude_domain = fields.Char(compute='_onchange_line', readonly=True, store=False)



    @api.depends('order_line')
    @api.onchange("order_line")
    def _onchange_line(self):
        self.exclude_domain = [line.product_id.id for line in self.order_line if line.product_id]


class SalesOrderLinesInherit(models.Model):
    _name = "sale.order.line"
    _inherit = "sale.order.line"

    express_delivery = fields.Boolean(default=False, string='Express delivery')

    @api.onchange('product_id')
    def _on_change_product_id(self):
        exclude_domain = json.loads(self.order_id.exclude_domain)

        return {'domain': {'product_id': [('sale_ok', '=', True), ('id','not in', exclude_domain), '|', ('company_id', '=', False), ('company_id', '=', self.order_id.company_id)]}}
