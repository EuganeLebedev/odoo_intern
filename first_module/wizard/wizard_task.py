# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WizardTask(models.TransientModel):
    _name = 'first_module.wizard_task'
    _description = "Wizard task"

    name = fields.Char(required=True)
    is_company = fields.Boolean()

    def action_wizard_task(self):
        return {
            'name': 'Create partner from wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'context': {'default_name': self.name,
                        'default_is_company': False},
        }
