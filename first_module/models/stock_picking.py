from odoo import fields, models, api
from copy import deepcopy


# class StockMoveInherit(models.Model):
#     _name = 'stock.move'
#     _inherit = 'stock.move'
#
#     @api.model
#     def create(self, vals_list):
#         print('CREATE METHOD FROM PICKING', vals_list)
# #         return 1/ 0
# # #         # return super().create(vals_list)
# # #
