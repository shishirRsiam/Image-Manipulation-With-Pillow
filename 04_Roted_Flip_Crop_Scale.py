import os
from PIL import Image, ImageDraw, ImageFont  # Importing necessary modules from Pillow (PIL) for image manipulation

# Open the original image
image = Image.open('mee1.jpg')

# Rotate the image by 20 degrees, expand the canvas to fit the rotated image, and fill the background with gray
img = image.rotate(20, expand=True, fillcolor='gray')
# image.show()  # Uncomment this line to view the original image
# img.show()     # Uncomment this line to view the rotated image

# Flip the image horizontally (mirror image)
image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

# Flip the image vertically (upside down)
image_flip_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

# Rotate the image 90 degrees (clockwise)
flip_180 = image.transpose(Image.Transpose.ROTATE_90)
# flip_180.show()  # Uncomment to display the rotated image

# Crop the image with the given box coordinates (left, top, right, bottom)
# This extracts the region from (550, 250) to (1550, 2600)
image_crop = image.crop((550, 250, 1550, 2600))
# image_crop.show()  # Uncomment to see the cropped image

# Create a new image size that is double the original width and height
new_image_size = (image.size[0] * 2, image.size[1] * 2)

# Resize the image to the new (larger) size
better_image = image.resize(new_image_size)
# better_image.show()  # Uncomment to display the resized image

# Save the resized image to a folder named 'Manipulated_Image' with a new filename
better_image.save(os.path.join('Manipulated_Image', '04_better_me.jpg'))