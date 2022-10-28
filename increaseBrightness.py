from importPil import *

image = Image.open('IMG_0486.jpg')

enhancer = ImageEnhance.Brightness(image)

factor = 1.5 #brightens the image
im_output = enhancer.enhance(factor)
im_output.save('brightened-image.png')