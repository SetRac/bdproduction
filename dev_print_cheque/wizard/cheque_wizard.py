# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Devintelle Software Solutions (<http://devintellecs.com>).
#
##############################################################################
from odoo import models,fields, api, _

class cheque_wizard(models.TransientModel):

    _name ='cheque.wizard'

    @api.model
    def get_company_id(self):
        return self.env.user.company_id.id
        
    @api.model
    def get_currency_id(self):
        return self.env.user.company_id.currency_id.id

    customer_name = fields.Char('Name', required="1")
    amount = fields.Float('Amount' , required="1")
    company_id = fields.Many2one('res.company','Company',default=get_company_id)
    date = fields.Date('Date', required="1")
    cheque_formate_id = fields.Many2one('cheque.setting',string='Cheque Formate',required="1")
    currency_id = fields.Many2one('res.currency',string='Currency',default=get_currency_id)
    
    @api.multi
    def print_report(self):
        data = self.read()
        datas = {
            'form': self.ids
        }
        return self.env.ref('dev_print_cheque.action_report_print_cheque_wizard').report_action(self, data=datas)
    
    



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
