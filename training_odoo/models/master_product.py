from odoo import fields, api, models
from datetime import datetime, timedelta


class MasterProduct(models.Model):
    _name = 'master.product'
    _description = 'Master Product'

    name = fields.Char('Product Name')
    prod_img = fields.Binary('Prod Img')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")
    field_name = fields.Boolean('Field Name')
    quantity = fields.Float('Quantity')
    harga_jual = fields.Float('Harga Jual')
    harga_modal = fields.Float('harga')
    type_product = fields.Selection([('consum', 'Produk Konsumsi'), ('jasa', 'Jasa'), ('store', 'Produk yang dapat disimpan')])
    kode_ref = fields.Char('Referensi Internal')

    def scheduler_favorite_reorder(self):
        prod = self.env['master.product'].search([])
        for p in prod:
            if p.quantity <= 1 and p.field_name:
                print(prod, 'ptiasdasdasdras')
                self.env['master.purchase'].create({
                    'tanggal_faktur': datetime.now(), 
                    'master_product_ids': [(0, 0, {'product_id': p.id, 'quantity': 10})]
                })
            


class MasterProductLine(models.Model):
    _name = 'master.product.line'
    _description = 'Master Product Line'

    product_id = fields.Many2one('master.product', string='Product')
    quantity = fields.Float('Quantity')
    unit_price = fields.Float('Unit Price')
    purchase_id = fields.Many2one('master.purchase', string='vendor')
    sales_id = fields.Many2one('master.sales', string='sale')

