# -*- coding: utf-8 -*-

from odoo import fields, models


# inherit sale order
class SaleOrder(models.Model):
    _inherit = "sale.order"

    child_ids = fields.Many2many('res.partner', string='Customer')
