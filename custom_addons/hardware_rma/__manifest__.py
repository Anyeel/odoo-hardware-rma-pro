{
    'name': 'Gestión de RMA y Garantías',
    'version': '1.0',
    'category': 'Inventory/Hardware',
    'summary': 'Sistema de gestión de devoluciones y garantías para hardware',
    'author': 'Ángel Millán',
    'depends': ['base', 'stock', 'mail'],  # Dependemos de "stock" porque manejamos productos físicos
    'data': [
        'security/ir.model.access.csv', # Esto lo crearemos ahora, no te preocupes si no existe
        'data/ir_sequence_data.xml',
        'views/rma_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}