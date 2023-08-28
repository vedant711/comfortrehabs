import pyqrcode

url = 'https://comfortrehabs.com/pdfs/catalog'

qr = pyqrcode.create(url)

qr.png('catalog.png',scale=10)