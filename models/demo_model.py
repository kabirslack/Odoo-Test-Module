# models/demo_model.py
from odoo import models, fields

class DemoModel(models.Model):
    _name = 'demo.model'
    _description = 'Demo Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
