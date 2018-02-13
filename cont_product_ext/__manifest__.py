# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Continuant Product Extenstion",
    'version': "1.1",
    'category': "sales",
    'sequence': 2,
    'summary': "Extend product",
    'description': """""",
    'author': "Bista solutions Pvt Ltd",
    'website': "https://www.bistasolutions.com",
    'images': [],
    'depends': [
        'product'
    ],
    # data files always loaded at installation
    'data': [
        'views/inherited_product_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
