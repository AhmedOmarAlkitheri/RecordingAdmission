from odoo import models, fields

class RcoredingAdmissionManage(models.Model):
    _name = 'recording.admission.manage'
    _description = 'Rcoreding Admission'

    name = fields.Char(string='Name')
    type = fields.Char(string='Type')
    employee = fields.Char(string='Employee')
    date = fields.Datetime(string='Date',default=fields.Datetime.now)


