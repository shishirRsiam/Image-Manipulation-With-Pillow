import os
from PIL import Image

# Open the image file
image = Image.open("love.jpg")

# Print image information
print(image.size)    # Outputs (width, height)
print(image.format)  # Outputs the format (e.g., 'JPEG', 'PNG')
print(image.mode)    # Outputs the mode (e.g., 'RGB', 'L')

# Resize the image to 10000x10000 pixels (may distort or enlarge it heavily)
resized_image = image.resize((10000, 10000))  # (width, height)
# resized_image.show()  # Uncomment to display the resized image

# Create a thumbnail version of the image (max size 100x100), maintains aspect ratio
thumbnail = image.copy()            # Work on a copy so original isn't affected
thumbnail.thumbnail((100, 100))     # Resize with aspect ratio preserved
# thumbnail.show()  # Uncomment to display the thumbnail

# Crop a portion of the image from (left=0, upper=0) to (right=400, lower=100)
cropped_image = image.crop((0, 0, 400, 100))
# cropped_image.show()  # Uncomment to display the cropped section

# Rotate the image by 45 degrees (may introduce black corners)
rotated = image.rotate(45)
# rotated.show()  # Uncomment to display the rotated image

# Flip the image horizontally (mirror effect)
flipped = image.transpose(Image.FLIP_LEFT_RIGHT)
# flipped.show()  # Uncomment to display the flipped image

# Convert the image to grayscale (L = luminance)
gray = image.convert("L")
gray.show()  # Display the grayscale image

# Save the grayscale image in a folder named 'Manipulated_Image'
# Create the folder if it doesn't exist
os.makedirs("Manipulated_Image", exist_ok=True)
gray.save(os.path.join("Manipulated_Image", "love_gray.jpg"))  # Save the grayscale image


# Close the image file
image.close()