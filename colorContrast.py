from importPil import *

image = Image.open('IMG_0486.jpg')

img_data = np.array(image)
print(img_data.shape)

#image brightness enhancer
enhancer = ImageEnhance.Contrast(image)

factor = 1.25 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('more-contrast-image.png')