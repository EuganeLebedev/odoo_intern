from odoo import fields, models, api
from copy import deepcopy


class StockMoveInherit(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'
    express_delivery = fields.Boolean(default=False)


