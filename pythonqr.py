import pyqrcode
from pyqrcode import QRCode
link=input()


ss="link.svg"
url=pyqrcode.create(link)
url.svg(ss, scale = 8)
