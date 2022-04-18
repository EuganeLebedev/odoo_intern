from odoo import models, fields, api
from odoo.exceptions import ValidationError

#TODO
# Добавить возможность изменить главный контакт
# Вывод атрибута главного контакта в kanban view

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
                raise ValidationError('Главный контакт может быть только один')
                # print(self.env.context.get('parent_id'))
                # contacts = self.env['res.partner'].search([('parent_id', '=', self.parent_id.id)])
                # for rec in contacts:
                #     print(rec.name)
                #     rec.is_primary = False
                # for rec in self.parent_id.child_ids:
                #     if rec.is_primary:
                #         print(rec.id)
                #         rec.is_primary = False
        else:
            if self.primary_contact_count == 0:
                raise ValidationError('Необходимо указать хотя бы один главный контакт')

    def unlink(self):
        if self.is_primary:
            raise ValidationError('Вы не можете удалить главный контакт')
        return super().unlink()
