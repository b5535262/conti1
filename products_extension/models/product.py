# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    ext_tax_code = fields.Text(string="External Tax Code")
    sales_tax_status = fields.Selection([('taxable', 'Taxable'),
                                         ('exempt', 'Exempt'),
                                         ('exempt_for_qualifying_accounts',
                                        'Exempt for Qualifying Accounts')],
                                        string="Sales Tax Status")
