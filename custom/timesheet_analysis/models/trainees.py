# -*- coding: utf-8 -*-


from odoo import models, fields, api


class Trainees(models.Model):
    _name = 'trainees'
    _description = "trainees"

    name = fields.Char(string='Name', required=True, )
    project = fields.Char(string='Project', required=True, )
    task = fields.Char(string='Task', required=True, )
    note = fields.Text(string='Description')
