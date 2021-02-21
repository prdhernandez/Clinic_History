# -*- encoding: utf-8 -*-
{
    'name': 'Clinic History Advanced',
    'version': '1.0',
    'author': 'EEP - Profesor',
    'description': """ Modulo extension de clinic history.""",
    'depends': ['clinichistory_app','mail'],
    'data': [
        'views/chadvanced_app.xml',
        'security/ir.model.access.csv',
        ],
}