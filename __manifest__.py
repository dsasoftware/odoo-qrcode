{
    'name': "Webcam Qrcode Scanner",
    'version': '13.0.0.1',
    'depends': ['base'],
    'author': "DevSanx",
    'category': "Sales/Sales",
    'summary': 'Qrcode/Barcode Scanner',
    'description': """
        Scan Barcodes and Qrcodes using device camera
    """,
    'data': [
        'views/assets.xml',
    ],
    'assets': {
        'web.assets_backend': [
            "odoo-qrcode/static/src/css/webcam_qrcode_scan_styles.css",
            "odoo-qrcode/static/src/lib/html5-qrcode.min.js",
            "odoo-qrcode/static/src/lib/quagga.min.js",
            "odoo-qrcode/static/src/js/barcode_scanner_widget.min.js",
            "odoo-qrcode/static/src/xml/webcam_qrcode_scan_template.xml"   
        ]
    },
    'installable': True,
}