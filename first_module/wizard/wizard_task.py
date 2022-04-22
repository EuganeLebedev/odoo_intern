# -*- coding: utf-8 -*-

from odoo import models, fields


class WizardTask(models.TransientModel):
    _name = 'first_module.wizard.task'
    _description = "Wizard task"

    name = fields.Char(required=True)
    is_company = fields.Boolean()

    def action_create_person(self):
        return {
            'name': 'Create person from wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'context': {'default_name': self.name,
                        'default_is_company': False},
        }

    def action_open_create_partner_form(self):
        return {
            'name': 'Create partner from wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env.ref('first_module.first_module_create_partner_view_form').id,
            'target': 'new',
            'res_model': 'first_module.wizard.task',
            'type': 'ir.actions.act_window',
            'context': {},
        }

    def action_create_partner(self):
        vals = {
            'name': self.name,
            'is_company': self.is_company
        }

        partner_rec = self.env['res.partner'].create(vals)

        return {
            'name': 'Created partner',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'res.partner',
            'res_id': partner_rec.id,
        }
