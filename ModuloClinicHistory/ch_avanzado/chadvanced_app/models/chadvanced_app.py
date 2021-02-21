#-*- coding: utf-8 -*-
from odoo import models, fields, api
class ClinicHistory(models.Model):
    _name = 'clinichistory'
    _inherit = ['clinichistory','mail.thread']
    is_admitted = fields.Boolean('Ingresado?')
    days_admitted = fields.Integer('Dias ingresado')
    episode_ids=fields.One2many('episodio', 'clinichistory_id')

    def do_marcar(self):
        self.is_admitted = not self.is_admitted
        return True

class Episodio(models.Model):
    _name = 'episodio'
    clinichistory_id=fields.Many2one('clinichistory', 'Request', ondelete='cascade')
    especialidad=fields.Char('Especialidad')
    user_id=fields.Many2one('res.users', 'Medico responsable')
    description = fields.Text('Descripcion', required=True)
    diagnostico=fields.Text('Diagnostico')