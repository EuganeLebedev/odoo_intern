from odoo import models, fields
from itertools import groupby

class StockMoveInherit(models.Model):
    _inherit = 'stock.move'
    express_delivery = fields.Boolean()

    def _search_picking_for_assignation(self):
        """
        Метод переопределен для добавления групировки по атрибуту express_delivery
        """
        self.ensure_one()
        picking = self.env['stock.picking'].search([
            ('group_id', '=', self.group_id.id),
            ('location_id', '=', self.location_id.id),
            ('location_dest_id', '=', self.location_dest_id.id),
            ('picking_type_id', '=', self.picking_type_id.id),
            ('printed', '=', False),
            ('express_delivery', '=', self.express_delivery),
            ('immediate_transfer', '=', False),
            ('state', 'in', ['draft', 'confirmed', 'waiting', 'partially_available', 'assigned'])], limit=1)
        # if picking.express_delivery == self.express_delivery:
        #     return picking
        return picking

    def _assign_picking(self):
        """
         Метод переопределен для групировки moves в том числе и по атрибуту express_delivery строк отгрузки
         Также при создании отгрузки, в строки которой входят позиции с атрибутом express_delivery, сама огрузка также
         получает атрибут express_delivery = True
         """
        Picking = self.env['stock.picking']
        grouped_moves = groupby(sorted(self, key=lambda m: [f.id for f in m._key_assign_picking()]),
                                key=lambda m: [m._key_assign_picking(), m.express_delivery])
        for group, moves in grouped_moves:
            moves = self.env['stock.move'].concat(*list(moves))
            new_picking = False
            # Could pass the arguments contained in group but they are the same
            # for each move that why moves[0] is acceptable
            picking = moves[0]._search_picking_for_assignation()
            if picking:
                if any(picking.partner_id.id != m.partner_id.id or
                       picking.origin != m.origin for m in moves):
                    # If a picking is found, we'll append `move` to its move list and thus its
                    # `partner_id` and `ref` field will refer to multiple records. In this
                    # case, we chose to  wipe them.
                    picking.write({
                        'partner_id': False,
                        'origin': False,
                    })
            else:
                new_picking = True
                picking = Picking.create(moves._get_new_picking_values())
                picking.write({'express_delivery': moves[0].express_delivery})

            moves.write({'picking_id': picking.id})
            moves._assign_picking_post_process(new=new_picking)
        return True

