from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    is_primary = fields.Boolean(string='Primary', default=False)

    @property
    def primary_contact_count(self):
        self._primary_contacts_count = len(list(filter(lambda record: record.is_primary == True, self.parent_id.child_ids)))
        return self._primary_contacts_count

    @api.onchange('is_primary')
    def _on_change_is_primary(self):
        if self.is_primary:
            if self.primary_contact_count > 1:
                partner_id = self.parent_id._origin.id
                # raise ValidationError('Главный контакт может быть только один')

                contacts = self.env['res.partner'].search([('parent_id', '=', partner_id),
                                                           ('id', '!=', self._origin.id),
                                                           ('is_primary', '=', True)])
                for rec in contacts:
                    rec.is_primary = False
        else:
            if self.primary_contact_count == 0:
                raise ValidationError('Необходимо указать хотя бы один главный контакт')

    def unlink(self):
        if self.is_primary:
            raise ValidationError('Вы не можете удалить главный контакт')
        return super().unlink()
