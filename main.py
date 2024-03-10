# import qrcode as qr
# img = qr.make("https://www.google.com")
# img.save("qrcode.png")

import qrcode
from PIL import Image

qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )

qr.add_data("https://www.google.com")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save("qrcode.png")