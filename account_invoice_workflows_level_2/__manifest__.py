{
    'name':   'Accounting Workflows (Level 2)',
    'author': 'Hafeez Brothers',
    'version': '1.0',
    'depends': [
                'base',
                'account',
                'purchase',
                'sale'
                
                ],
    
    'data': [
      
        'Views/account_invoice_workflows.xml',
        'security/hr_user_rights_invoice.xml'
    ],
    
    'application': True,
    'price':40.00,
    'currency':'EUR', 

}
