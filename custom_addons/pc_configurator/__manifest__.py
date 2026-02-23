{
    'name': 'PC Configurator Pro',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Configurador de equipos informáticos con reglas de compatibilidad',
    'description': """
        Módulo avanzado para presupuestar PCs a medida validando 
        la compatibilidad entre Socket, RAM y Placa Base.
    """,
    'author': 'Ángel Millán',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/pc_build_views.xml',
        'views/pc_menus.xml',
    ],
    'installable': True,
    'application': True,
}