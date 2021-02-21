# -*- coding: utf-8 -*-
from odoo import models, fields
class ClinicHistory(models.Model):
    _name = 'clinichistory'
    _description = 'Clinic History'
    n_history = fields.Char('NHistoria', required=True)
    identification= fields.Char('ID', required=True)
    name = fields.Char('Nombre', required=False)
    __last_update = fields.Date('Ultima modficacion', required=False)