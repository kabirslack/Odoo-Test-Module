# __manifest__.py
{
    'name': 'Demo Module',
    'version': '1.0',
    'summary': 'A demo module for Odoo v17',
    'description': 'This module demonstrates basic functionality in Odoo v17.',
    'author': 'Your Name',
    'website': 'http://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/demo_view.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
