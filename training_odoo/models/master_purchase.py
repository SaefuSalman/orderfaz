from odoo import fields, api, models


class MasterPurchase(models.Model):
    _name = 'master.purchase'
    _description = 'Master Purchase'

    name = fields.Char('Faktur Pelanggan')
    vendor_id = fields.Many2one('master.vendor', string='Vendor')
    tanggal_faktur = fields.Date('Tanggal Faktur')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")
    master_product_ids = fields.One2many('master.product.line', 'purchase_id', string='Master Product')

    @api.model_create_multi
    def create(self, vals):
        supp = super(MasterPurchase, self).create(vals)
        for line in supp.master_product_ids:
            if line.product_id.id:
                self.env['master.product'].search([('id', '=', line.product_id.id)]).write({'quantity': line.quantity})
            else:
                continue
        return supp

