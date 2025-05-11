import os
from PIL import Image, ImageDraw, ImageFont


image = Image.open('mee1.jpg')
img = image.rotate(20, expand=True, fillcolor='gray')
# image.show()
# img.show()


image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_flip_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
flip_180 = image.transpose(Image.Transpose.ROTATE_90)
# flip_180.show()


image_crop = image.crop((550, 250, 1550, 2600))
# image_crop.show()


new_image_size = (image.size[0] * 2, image.size[1] * 2)
better_image = image.resize(new_image_size)
# better_image.show()
better_image.save(os.path.join('Manipulated_Image', '04_better_me.jpg'))