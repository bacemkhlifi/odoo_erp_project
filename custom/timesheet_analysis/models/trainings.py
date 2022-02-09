# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class Trainings(models.Model):
    _name = "trainings"
    _description = "trainees"

    code = fields.Char(string='Code', required=True, )
    name = fields.Char(string='Training Name', required=True, )
    reference = fields.Char(string='Training Reference', readonly=True,
                            default=lambda self: _('New'))
    state = fields.Selection(
        string='Status',
        selection=[
            ('waiting','Waiting'),
            ('approved', 'Approved'),
                   ('in_progress', 'In Progress'),
                   ('done', 'Done'),
                   ('cancel','Cancelled')], default='waiting', tracking=True)
    trainer = fields.Many2one(
        comodel_name='res.partner',
        string='Trainer',
        required=False)
    def done_action(self):
        self.state = 'done'

    def in_progress_action(self):
        self.state = 'in_progress'
    def approved_action(self):
        self.state = 'approved'
    def cancel_action(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        # Add code here
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('trainings') or _('New')
        return super(Trainings, self).create(vals)