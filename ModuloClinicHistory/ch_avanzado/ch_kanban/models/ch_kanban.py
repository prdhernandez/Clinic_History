from odoo import models, fields
class ClinicHistory(models.Model):
    _inherit = 'clinichistory'
    priority = fields.Selection([
        ('0','Low'),
        ('1','Normal'),
        ('2','High')],
        'Priority',default='1')
    kanban_state = fields.Selection([
        ('normal', 'Not admitted'),
        ('admitted', 'Admitted')],
        'Kanban State',
        default='normal')