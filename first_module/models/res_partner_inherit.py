from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    is_primary = fields.Boolean(string='Primary', default=False)
    primary_contact = fields.Many2one('res.partner')
    is_primary_date = fields.Datetime(default=datetime.strptime('01/01/1970', '%d/%m/%Y'))

    @property
    def primary_contact_count(self):
        self._primary_contacts_count = len(list(filter(lambda record: record.is_primary == True, self.parent_id.child_ids)))
        return self._primary_contacts_count

    @api.onchange('child_ids')
    def _onchange_contact_ids(self):
        primapy_contact = [element for element in self.child_ids.filtered(lambda r: r.is_primary == True)]

        if len(primapy_contact) > 0:
            for n in range(len(primapy_contact) - 1, 0, -1):
                for i in range(n):
                    if primapy_contact[i].is_primary_date < primapy_contact[i + 1].is_primary_date:
                        primapy_contact[i], primapy_contact[i + 1] = primapy_contact[i + 1], primapy_contact[i]

        if len(primapy_contact) > 1:
            for contact in primapy_contact[1:]:
                contact.is_primary = False

    @api.onchange('is_primary')
    def _compute_is_primary_date(self):
        for rec in self:
            rec.is_primary_date = datetime.now()

    # @api.onchange('is_primary')
    # def _on_change_is_primary(self):
        # self.is_primary_date = datetime.now()
    #     if self.is_primary:
    #         if self.primary_contact_count > 1:
    #             partner_id = self.parent_id._origin.id
    #             # raise ValidationError('Главный контакт может быть только один')
    #
    #             contacts = self.env['res.partner'].search([('parent_id', '=', partner_id),
    #                                                        ('id', '!=', self._origin.id),
    #                                                        ('is_primary', '=', True)])
    #             for rec in contacts:
    #                 rec.is_primary = False
    #     else:
    #         if self.primary_contact_count == 0:
    #             raise ValidationError('Необходимо указать хотя бы один главный контакт')

    def unlink(self):
        if self.is_primary:
            raise ValidationError('Вы не можете удалить главный контакт')
        return super().unlink()
