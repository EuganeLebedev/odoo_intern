from odoo import  models, api, fields

#
class ProcurementGroupInherit(models.Model):

    _inherit = 'procurement.group'

    @api.model
    def run(self, procurements):
        super(ProcurementGroupInherit, self).run(procurements[0:1])
        super(ProcurementGroupInherit, self).run(procurements[1:2])
    #     super(ProcurementGroupInherit, self).run(procurements[1:2])
    #     super(ProcurementGroupInherit, self).run(procurements[2:3])

        # for procurement in procurements:
        #     tmp_list = []
        #     tmp_list.append(procurement)
        #     print(f"{tmp_list}")
        #     super().run(tmp_list)


# class StockMove(models.Model):
#     _inherit = "stock.move"
# 
#     def _action_confirm(self, merge=True, merge_into=False):
#         return super(StockMove, self)._action_confirm(merge=False)



# class StockRuleInherit(models.Model):
#     _inherit = 'stock.rule'


    # @api.model
    # def _run_pull(self, procurements):
    #     super(StockRuleInherit, self)._run_pull(procurements[0:1])
    #     super(StockRuleInherit, self)._run_pull(procurements[1:2])
    #     # for procurement in procurements:
    #     #     tmp_list = []
    #     #     tmp_list.append(procurement)
    #     #     print(f"{tmp_list}")
    #     #     super()._run_pull(tmp_list)
    #
    # @api.model
    # def run(self, procurements):
    #     super(StockRuleInherit, self).run(procurements[0:2])

# class StockRuleInherit(models.Model):
#     _inherit = 'stock.rule'
#
#     def _get_stock_move_values(self, *args):
#         print(args)