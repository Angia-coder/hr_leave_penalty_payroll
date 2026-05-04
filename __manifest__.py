{
    'name': 'HR Holiday Penalty',
    'version': '1.0',
    'summary': 'Penalty for wrong leave',
    'depends': ['hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_leave_views.xml',
    ],
    'installable': True,
    'application': False,
}
