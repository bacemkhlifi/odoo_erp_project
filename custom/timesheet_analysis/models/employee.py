# -*- coding: utf-8 -*-


from odoo import api, fields, models
class Employee(models.Model):
    _name = "employee"
    _description = "employee"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True,)
    age = fields.Integer(String='Age')
    project = fields.Char(string='Project', required=True, )
    task = fields.Char(string='Task', required=True, )
    note = fields.Text(string='Description')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')] , default= 'male'
    )
    role = fields.Selection(
        string='Role',
        selection=[('designer', 'Designer'),
                   ('developer', 'Developer'), ],
        required=False, )




