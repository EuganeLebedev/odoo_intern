from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class ResPartnerInherit(models.Model):
    """
    Добавлены поля
    is_primary - Атрибут, указывающий на то, что контакт является главным
    is_primary_date - Системное поле для отслеживания того, когда контакт был указан как главный
    """
    _inherit = 'res.partner'
    is_primary = fields.Boolean(string='Primary', default=False)
    is_primary_date = fields.Datetime(default=datetime.strptime('01/01/1970', '%d/%m/%Y'))

    @property
    def primary_contact_count(self):
        self._primary_contacts_count = len(
            list(filter(lambda record: record.is_primary == True, self.parent_id.child_ids)))
        return self._primary_contacts_count

    @api.onchange('child_ids')
    def _onchange_contact_ids(self):
        primapy_contact = [element for element in self.child_ids.filtered(lambda r: r.is_primary == True)]

        if len(primapy_contact) > 0:
            primapy_contact = sorted(
                primapy_contact,
                key=lambda rec: rec.is_primary_date if rec.is_primary_date else fields.Datetime.to_datetime('01/01/1970')
                , reverse=True
            )

        if len(primapy_contact) > 1:
            for contact in primapy_contact[1:]:
                contact.is_primary = False
                return {'warning': {'title': ("Warning"), 'message': 'Главный контакт может быть только один'}}

    @api.onchange('is_primary')
    def _compute_is_primary_date(self):
        for rec in self:
            rec.is_primary_date = datetime.now()

    def unlink(self):
        if self.is_primary and self.type == 'contact':
            raise ValidationError('Вы не можете удалить главный контакт')
        return super().unlink()
