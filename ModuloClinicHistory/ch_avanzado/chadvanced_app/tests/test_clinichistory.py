# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase
class TestClinichistory(TransactionCase):
    def test_create(self):
        "Create a clinic history"
        Clinichistory = self.env['clinichistory']
        history = Clinichistory.create({'name': 'Test history'})
        self.assertEqual(history.is_admitted, False)