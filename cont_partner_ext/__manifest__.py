# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Continuant Partner Extended',
    'version': '1.1',
    'category': 'Sales',
    'sequence': 1,
    'summary': 'This module contains customization about Customer form',
    'description': "",
    'website': 'http://www.bistasolutions.com',
    'depends': [
        'contacts',
        'sale_management',
        'account_accountant'
    ],
    'data': [
        'data/res.partner.industry.csv',
        'security/ir.model.access.csv',
        'views/partner_ex_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
