import pytesseract
from PIL import Image
# for i in range(2,10):
#     i = str(i)
image = Image.open('checked/CheckCode '+'('+"1"+')'+'.gif').convert("RGB")
image.show()
image = Image.open('checked/'+"1"+'.tiff')
vcode = pytesseract.image_to_string(image)
print vcode

# print '111'