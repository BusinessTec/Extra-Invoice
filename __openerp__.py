# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today OpenERP SA (<http://www.openerp.com>).
#    Copyright (C) 2014-Today Business Tec Systems SA (<http://www.businesstec.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Extra Invoice Layouts',
    'version': '1.0',
    'sequence': 18,
    'summary': 'Additional reports to be printed for invoice view',
    'description': """
Create additional printouts of invoices
=======================================
Adds additonal layout of invoice and button under Print drop down option.
This module requres manual corrections before installing in invoice_extra.xml and report in 
views folder to match final requirements (recommended use of branches to manage the processes. 
    """,
    'author': 'Business Tec Systems S.A.',
    'website': 'http://www.businesstec.net',
    'depends': ['sale', 'report'],
    'category': 'Sale',
    'data': ['views/report_invoice_extra_org.xml',
    'invoice_extra.xml'],
    'installable': True,
}
