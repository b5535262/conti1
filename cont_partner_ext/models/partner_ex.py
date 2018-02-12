from odoo import models, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    entity_lst = [('a', 'A - Federal government - United States'),
                  ('b', 'B - State government - United States'),
                  ('c', 'C - Tribe / Status Indian / Indian Band - both'),
                  ('d', 'D - Foreign diplomat - both'),
                  ('e', 'E - Charitable or benevolent org - both'),
                  ('f', 'F - Religious or educational org - both'),
                  ('g', 'G - Resale - both'),
                  ('h', 'H - Commercial agricultural production - both'),
                  ('i', 'I - Industrial production / manufacturer - both'),
                  ('j', 'J - Direct pay permit - United States'),
                  ('k', 'K - Direct mail - United States'),
                  ('l', 'L - Other - both'),
                  ('n', 'N - Local government - United States'),
                  ('p', 'P - Commercial aquaculture - Canada'),
                  ('q', 'Q - Commercial Fishery - Canada'),
                  ('r', 'R - Non-resident - Canada')]
    cust_status_list = [('unreg_pro', 'Unregistered Prospect'),
                        ('registered', 'Registered'),
                        ('service_trans', 'Service Transition'),
                        ('inactive', 'Inactive'),
                        ('isr', 'ISR'),
                        ('former_customer', 'Former Customer')]
    collector_list = [('agency', 'Agency'), ('bad_debt', 'Bad Debt'),
                      ('bankrupt', 'Bankrupt'),
                      ('coll_agency', 'Coll Agency'),
                      ('legal_settlement', 'Legal Settlement')]
    sale_tax_list = [('taxable', 'Taxable'), ('exempt', 'Exempt'),
                     ('exempt for qualified products',
                      'Exempt for Qualified Products')]
    inv_del_method = [('email', 'Email'), ('mail', 'Mail'), ('email_mail',
                      'Email And Mail'), ('portal', 'Portal')]
    oem_list = [('avaya', 'Avaya'), ('nortel', 'Nortel'), ('cisco', 'Cisco'),
                ('siemens/unify', 'Siemens/Unify'),
                ('microsoft', 'Microsoft'), ('dialer', 'Dialer'),
                ('other', 'Other'), ('cisco cloud', 'Cisco Cloud'),
                ('ms cloud', 'MS Cloud'),
                ('other cloud', 'Other Cloud')]
    account_name = fields.Char('Account Name')
    owner_id = fields.Many2one('res.users', 'Account Owner')
    record_type = fields.Char('Account Record Type')
    acc_trading_curr = fields.Text('Account Trading Currency')
    assigned_collector_id = fields.Many2one('res.users', 'Assigned Collector')
    collector_status = fields.Selection(collector_list, 'Collector Status')
    credit_limit_hierarchy = fields.Char('Credit Limit in Hierarchy')
    credit_risk = fields.Text('Credit Risk')
    cumulative_credit_val = fields.Float('Cumulative Credit value')
    cust_status = fields.Selection(cust_status_list, 'Customer Status')
    cust_tier = fields.Char('Customer Tier')
    duns_no = fields.Text('D-U-N-S Number')
    entity_code = fields.Selection(entity_lst, 'Entity / Use Code')
    is_hold_account = fields.Boolean('Hold Account')
    master_acc_id = fields.Many2one('account.account', 'Master Account')
    parent_acc_id = fields.Many2one('account.account', 'Parent Account')
    invoice_del_method = fields.Selection(inv_del_method, 'Preferred Invoice \
                        Delivery Method')
    oem_type = fields.Selection(oem_list, 'Primary OEM')
    sales_tax_status = fields.Selection(sale_tax_list, 'Sales Tax Status')
    acc_manager_id = fields.Many2one('res.users', 'Strategic Account Manager')
    former_account_name = fields.Text('Former Account Name')
