from importPil import *

image = Image.open('IMG_0486.jpg')

enhancer = ImageEnhance.Sharpness(image)

factor = 1.5
im_output = enhancer.enhance(factor)
im_output.save('sharp-image.png')