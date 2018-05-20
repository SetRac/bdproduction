# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Devintelle Software Solutions (<http://devintelle.com>).
#
##############################################################################

{
    'name': 'Dynamic Print Cheque - Check writing',
    'version': '1.0',
    'category': 'Account',
    'description': """
         App will  configure and print cheque/check Dynamically for any bank with different Cheque format.

Cheque print, check print, check writing, bank check print, check dynamic, bank cheque, cheque dynamic, cheque printing, bank cheque, dynamic print cheque, cheque payment, payment check, 

    """,
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'summary':'App will  configure and print cheque/check Dynamically for any bank with different Cheque format',
    'website': 'http://devintellecs.com/',
    'images': [],
    'depends': ['account','account_voucher'],
    'data': [
        'security/ir.model.access.csv',
        'views/report_print_cheque.xml',
        'wizard/cheque_wizard_view.xml',
        'views/report_print_cheque_wizard.xml',
#        'report/print_cheque_template.xml',
        'views/report_menu.xml',
        'views/cheque_setting_view.xml',
        'views/account_vocher_view.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'currency':'EUR',
    'live_test_url':'https://youtu.be/A5kEBboAh_k',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
