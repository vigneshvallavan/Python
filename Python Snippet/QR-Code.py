import pyqrcode
import png
from PIL import Image, ImageDraw

url = "https://github.com/vigneshvallavan"

# convert url into QR code
QR_code = pyqrcode.create(url)

# convert QR_code into image format with scale 6 (size)
QR_code.png('QR-code-Github.png', scale = 6)

# open QR code image file to add text
img = Image.open('QR-code-Github.png')

# Convert image into an editable format
d1 = ImageDraw.Draw(img)

# Decide the Text Location, color
d1.text( (55,10), "github - vigneshvallavan")

# Save the changes
img.save("QR-code-Github.png")

# view the image file directly
img.show()

