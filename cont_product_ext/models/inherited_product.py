# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    ext_tax_code = fields.Text(string="External Tax Code")
    inc_rec = fields.Boolean(string="Include in Rev Rec")
    sales_tax_status = fields.Selection([('taxable', 'Taxable'),
                                         ('exempt', 'Exempt'),
                                         ('exempt_for_qualifying_accounts',
                                        'Exempt for Qualifying Accounts')],
                                        string="Sales Tax Status")
    description = fields.Text(string="Description")
