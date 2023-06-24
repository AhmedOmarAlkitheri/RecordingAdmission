from odoo import models, fields

class CovenentRecordManage(models.Model):
    _name = 'covenent.record.manage'
    _description = 'Covenent Record'

    name = fields.Char(string='Name')
    type = fields.Char(string='Type')
    employee = fields.Char(string='Employee')
    date = fields.Datetime(string='Date',default=fields.Datetime.now)


