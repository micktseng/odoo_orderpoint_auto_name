from odoo import models, fields, api

class OrderPoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    @api.onchange('product_id', 'location_id')
    def onchange_auto_rename(self):
        self.name = 'OP/' + self.location_id.display_name + '/' +  self.product_id.name
