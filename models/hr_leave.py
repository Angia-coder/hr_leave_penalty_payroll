from odoo import models, fields, api

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    is_wrong_leave = fields.Boolean(string="Nghỉ sai quy định")

    penalty_rate = fields.Float(
        string="Hệ số phạt",
        default=1.0
    )

    penalty_hours = fields.Float(
        string="Penalty Hours",
        compute="_compute_penalty_hours",
        store=True
    )

    approved_by = fields.Many2one(
        'res.users',
        string="Approved By",
        readonly=True
    )

    @api.depends('number_of_hours_display', 'penalty_rate', 'is_wrong_leave')
    def _compute_penalty_hours(self):
        for rec in self:
            if rec.is_wrong_leave:
                rec.penalty_hours = rec.number_of_hours_display * rec.penalty_rate
            else:
                rec.penalty_hours = 0

    def action_approve(self):
        res = super().action_approve()
        for rec in self:
            rec.approved_by = self.env.user.id
        return res
