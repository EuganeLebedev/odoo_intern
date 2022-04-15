# -*- coding: utf-8 -*-

from odoo import models, fields

class FirstModel(models.Model):
    _name = 'first_module.first_model'
    _description = 'My first model'

    name = fields.Char()
    description = fields.Text()
    record_date = fields.Date()
    active = fields.Boolean(default=True, string="Is active")

