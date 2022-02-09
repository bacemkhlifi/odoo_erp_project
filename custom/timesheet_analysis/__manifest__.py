# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'TimeSheets',
    'version' : '1.1',
    'summary': 'timesheet analysis',
    'sequence': -100,
    'description': """
timesheet analysis 
    Perform timesheet analysis
    Perform leave analysis
    Perform the detection of imputation errors and their treatment
    Generate monthly activity reports
""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee.xml',

        'views/trainings.xml',
        'data/data.xml',
        'views/developer.xml',
        'views/designer.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
