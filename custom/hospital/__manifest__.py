# -*- coding: utf-8 -*-
{
    'name': "hospital",
    'summary': "Hospital management",
    'description': """ Long description of module's purpose """,

    'author': "SOLOFONDRAIBE Donné Alphonse",
    'website': "https://www.dannidotcon.github.io/portfolio",

    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'mail', 'board'],

    # always loaded
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/hospital_menu.xml",
        "wizards/create_appointment.xml",
        "views/hospital_doctor_views.xml",
        #"views/sale_order_views.xml",
        "views/hospital_lab_views.xml",
        "views/hospital_appointment_views.xml",
        "views/hospital_patient_views.xml",
        "views/hospital_dashboard.xml",
        "reports/patient_card.xml",
        "reports/report.xml",
        "data/mail_template.xml",
        
    ],
    # only loaded in demonstration mode
  
    'demo': [
        'demo/demo.xml',
    ],
}

