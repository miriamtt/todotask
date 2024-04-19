# -*- coding: utf-8 -*-
{
    'name': "moduloprueba",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm_claim'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
        'views/category.xml',
        'views/stage.xml',
        'data/todo_task_data.xml',
        'views/reporting.xml',
        'views/contacts.xml',
        'security/access_rules.xml',
        # 'controllers/*',
        # 'views/templates.xml',
    ],
    'installable': True, 
    'applicaction': True,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # icon of module
    'images': ['static/description/icono.png'],

}

