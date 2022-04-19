from odoo import models, fields, api
import re

class PolishTest(models.Model):
    _name = 'first_module.polish.test'
    _description = 'Polish test'

    text = fields.Text(default='')
    check1 = fields.Boolean(string='Test 1')
    check2 = fields.Boolean(string='Test 2')
    check_all = fields.Boolean(string='Select all')
    select1 = fields.Selection([('1','1'),('2','2'),('3','3')])
    select2 = fields.Selection([('4','4'),('5','5'),('6','6')])
    boolean1 = fields.Boolean(string='1')
    boolean2 = fields.Boolean(string='2')
    boolean3 = fields.Boolean(string='3')
    boolean4 = fields.Boolean(string='4')
    boolean5 = fields.Boolean(string='5')
    boolean6 = fields.Boolean(string='6')
    boolean7 = fields.Boolean(string='7')
    boolean8 = fields.Boolean(string='8')
    boolean9 = fields.Boolean(string='9')

    @api.onchange('check_all')
    def _on_change_check_all(self):
        self.check1 = self.check_all
        self.check2 = self.check_all

    @api.onchange('check1')
    def _on_change_check1(self):
        field_label = self.fields_get('check1')['check1']['string']

        if self.check1:
            if len(self.text) > 0:
                self.text = self.text + ' '
            self.text = (self.text + f'[{field_label}]').strip()
        else:
            pattern = f'\[{field_label}\]'
            self.text = re.sub(pattern, '', self.text).strip()

    @api.onchange('check2')
    def _on_change_check2(self):
        field_label = self.fields_get('check2')['check2']['string']
        if self.check2:
            if len(self.text) > 0:
                self.text = self.text + ' '
            self.text = (self.text + f'{{{field_label}}}').strip()
        else:
            pattern = f'{{{field_label}}}'
            self.text = re.sub(pattern, '', self.text).strip()

    @api.onchange('select1')
    def _on_change_select1(self):
        if self.select2 and self.select1:
            self.select2 = False

    @api.onchange('select2')
    def _on_change_select2(self):
        if self.select1 and self.select2:
            self.select1 = False
