{
    'name': 'Recording_Admission_menagment',
    'version': '1.0.0',
    'sequence': -100,
    'author': 'Ahmed Alkitheri',
    'website': ['www.Alkitheri','.com'],
    'category': 'Recording',
    'summary': 'Recording management system',
    'description': 'Recording management system',
    'depends': ['base'],
    'data': [
        'views/Recording_Admission_views.xml',
        'security/ir.model.access.csv',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
