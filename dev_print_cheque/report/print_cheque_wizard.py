# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Devintelle Software Solutions (<http://devintellecs.com>).
#
##############################################################################
#import time
from datetime import datetime, timedelta
from odoo import api, models
from odoo.tools import amount_to_text_en

class print_cheque_wizard(models.AbstractModel):
    _name = 'report.dev_print_cheque.cheque_report'

    @api.model
    def render_html(self, docids, data=None):
        doc = self.env['cheque.wizard'].browse(docids) 
        docargs = {
            'doc_ids': docids,
            'doc_model': 'cheque.wizard',
            'docs': doc,
        }
        return self.env['report'].render('dev_print_cheque.cheque_report', docargs)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
