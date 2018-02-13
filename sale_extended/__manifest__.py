# -*- coding: utf-8 -*-

{
    'name': 'Sale Extended',
    'version': '1.2',
    'category': 'Sale',
    'sequence': 3,
    'summary': 'Sale',
    'website': 'https://www.bistasolutions.com',
    'author': 'Bista Solutions',
    'description': """
* Customization in Sale order, add Button and make wizard
""",
    'depends': ['sale'],
    'data': [
            'wizard/customer_location_wizard_view.xml',
            'views/sale_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
