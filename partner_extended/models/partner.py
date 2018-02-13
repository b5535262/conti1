from odoo import models, fields


class EntityCode(models.Model):

    _name = 'entity.code'

    name = fields.Char('Name')
    code = fields.Char('Code')


class InvDeliveryMethod(models.Model):

    _name = 'inv.delivery.method'

    name = fields.Char('Name')
    code = fields.Char('Code')


class PrimaryOem(models.Model):

    _name = 'primary.oem'

    name = fields.Char('Name')
    code = fields.Char('Code')


class CollectorStatus(models.Model):

    _name = 'collector.status'

    name = fields.Char('Name')
    code = fields.Char('Code')


class ResPartner(models.Model):

    _inherit = 'res.partner'

    cust_status_list = [('unreg_pro', 'Unregistered Prospect'),
                        ('registered', 'Registered'),
                        ('service_trans', 'Service Transition'),
                        ('inactive', 'Inactive'),
                        ('isr', 'ISR'),
                        ('former_customer', 'Former Customer')]
    sale_tax_list = [('taxable', 'Taxable'), ('exempt', 'Exempt'),
                     ('exempt for qualified products',
                      'Exempt for Qualified Products')]
    assigned_collector_id = fields.Many2one('res.users', 'Assigned Collector')
    collector_status_id = fields.Many2one('collector.status',
                                          'Collector Status')
    cust_status = fields.Selection(cust_status_list, 'Customer Status')
    sales_tax_status = fields.Selection(sale_tax_list, 'Sales Tax Status')
    duns_no = fields.Text('D-U-N-S Number')
    entity_code_id = fields.Many2one('entity.code', 'Entity / Use Code')
    is_hold_account = fields.Boolean('Hold Account')
    invoice_del_method_id = fields.Many2one('inv.delivery.method', 'Preferred \
                            Invoice Delivery Method')
    oem_type_id = fields.Many2one('primary.oem', 'Primary OEM')
    acc_manager_id = fields.Many2one('res.users', 'Strategic Account Manager')
    former_account_name = fields.Text('Former Account Name')
