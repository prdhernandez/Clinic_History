{
    'name': 'Clinic-History Application', 
    'version': '1.0',
    'description': 'Manage clinic-histories',
    'author': 'Paula Rodriguez',
    'depends': ['base'],
    'application': True,
    'data' : [
        'security/ir.model.access.csv',
        'views/clinichistory_app.xml',
    ],
}