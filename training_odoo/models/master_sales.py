from odoo import fields, api, models, _
from odoo.exceptions import UserError


class MasterSales(models.Model):
    _name = 'master.sales'
    _description = 'Master Sales'

    name = fields.Char('Name')
    order_date = fields.Datetime('Order Date')
    product_line_ids = fields.One2many('master.product.line', 'sales_id', string='product')

    @api.model_create_multi
    def create(self, vals):
        supp = super(MasterSales, self).create(vals)
        for line in supp.product_line_ids:
            if line.product_id.id and line.product_id.quantity > line.quantity or line.product_id.quantity == line.quantity:
                new_quantity = line.product_id.quantity - line.quantity
                self.env['master.product'].search([('id', '=', line.product_id.id)]).write({'quantity': new_quantity})
            else:
                raise UserError(_(f"persedian stock, {line.product_id.quantity}"))
        return supp