{
  'name': 'Sumex Imports Csv',
  'description': 'Interfaz de importaciones CSV',
  'author': 'Sumex S.A.',
  'depends': ['base', 'contacts', 'account', 'stock', 'sale_management'],
  'data': [
    'security/ir.model.access.csv',
    'wizard/csv_instructions_wizard_forms.xml',
    'views/forms.xml',
    'views/menu.xml',
  ],
  'application': True,
  'installable': True,
}
