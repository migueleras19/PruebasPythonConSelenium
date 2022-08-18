import pyqrcode
from pyqrcode import QRCode

x = 'https://twitter.com/MiguelEras/'
a = 'https://www.linkedin.com/in/migueleras/'

xruta = pyqrcode.create(x)
xruta1 = pyqrcode.create(a)


xruta.svg("twitteruser.svg", scale=8)
xruta1.svg("linke.svg", scale=8)
