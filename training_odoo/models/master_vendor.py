from odoo import fields, api, models


class MasterVendor(models.Model):
    _name = 'master.vendor'
    _description = 'Master Vendor'

    name = fields.Char('Name')
    email = fields.Char('email')
