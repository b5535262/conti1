# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleCustomerWizard(models.TransientModel):
    _name = "sale.customer.wizard"

    customer_ids = fields.One2many('sale.customer.line',
                                   'line_id', string="Customers")
    partner_id = fields.Many2one('res.partner', string="Customer")
    total_qty = fields.Float(string="Total Qty")
    remaining_qty = fields.Float(string="Remaining Qty")

    # get active_id and Customer from Current sale order
    @api.onchange('partner_id')
    def onchange_res_partner(self):
        sale_id = self.env['sale.order'].browse(self.env.context['active_id'])
        if sale_id.order_line:
            qty_total = 0.0
            for line in sale_id.order_line:
                qty_total += line.product_uom_qty
            self.total_qty = qty_total

        if sale_id:
            res_customer = []
            for i in sale_id.child_ids:
                res = {}
                res['partner_id'] = i.id
                res_customer.append(res)
            self.customer_ids = res_customer

    # UserError if Qty is not same in wizard
    @api.multi
    def assign_location(self):
        if self.customer_ids:
            qty_total = 0.0
            for line in self.customer_ids:
                qty_total += line.qty
            total_qty = qty_total
            if total_qty != self.total_qty:
                raise UserError(_('Qty is not same.'))

    @api.multi
    def assign_equaly_qty(self):
        print("*******assign_equaly_qty*******")

    @api.multi
    def assign_remaining_qty(self):
        print("^^^^^^assign_remaining_qty^^^^^^^")

class SaleCustomerLine(models.TransientModel):
    _name = "sale.customer.line"

    line_id = fields.Many2one('sale.customer.wizard', string="Customer Line")
    partner_id = fields.Many2one('res.partner', string="Customer")
    qty = fields.Float(string="Qty")
