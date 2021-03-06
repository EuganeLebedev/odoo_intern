# -*- coding: utf-8 -*-
{
    'name': "First module",

    'summary': """
        My first module from task 1""",

    'description': """
        My first module from task 1
    """,

    'author': "E Lebedev",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/first_module_first_model_view.xml',
        'views/first_module_polish_test_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_line_view.xml',
        'views/stock_picking_view.xml',

        'wizard/first_module_wizard_task_vies.xml',

        'views/fist_module_menus_view.xml',

        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'licence': 'LGPL-3'
}
