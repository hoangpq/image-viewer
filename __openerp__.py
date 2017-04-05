{
    'name': 'Image Viewer',
    'author': 'Hoang Phan, pquochoang2007@gmail.com',
    'category': 'Hidden',
    'version': '1.0',
    'description': ''' Odoo addon help you to view images without downloading ''',
    'depends': ['base', 'web'],
    'auto_install': False,
    'data': [
        'views/image_viewer.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
}
