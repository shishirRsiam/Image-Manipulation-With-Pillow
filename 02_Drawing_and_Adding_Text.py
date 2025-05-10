import os
from PIL import Image, ImageDraw, ImageFont

# Open the image
image = Image.open("love.jpg")

# Create a drawing object to draw on the image
draw = ImageDraw.Draw(image)

# Load a TrueType font (make sure arial.ttf exists on your system)
font = ImageFont.truetype("arial.ttf", 50)

# ========== DRAWING SHAPES ==========

# Draw a red diagonal line from (left=50, upper=50) to (right=100, lower=300) with width 5
draw.line((50, 50, 100, 300), fill="red", width=5)

# Draw a green rectangle from (left=100, upper=100) to (right=200, lower=200)
draw.rectangle((100, 100, 200, 200), fill="green")

# Draw a green text "Sishir Siam" at (x=300, y=500)
draw.text((300, 500), "Sishir Siam", font=font, fill="green")

# Draw a filled green ellipse inside the bounding box:
# left=200, upper=200, right=300, lower=300
draw.ellipse((200, 200, 300, 300), fill="green")

# Draw a green filled triangle with a black outline using three points
# Each tuple is (x, y) coordinate
draw.polygon([(100, 100), (150, 50), (200, 100)], fill="green", outline="black")

# Draw a purple arc (half-circle) from angle 0 to 180 inside the box:
# left=150, upper=150, right=250, lower=250
draw.arc((150, 150, 250, 250), start=0, end=180, fill="purple", width=3)

# Draw a filled orange chord (like an arc with a straight line) inside same box:
# left=150, upper=150, right=250, lower=250
draw.chord((150, 150, 250, 250), 0, 180, fill="orange", outline="black")

# Draw a pink pie slice from 0 to 90 degrees inside the box:
# left=200, upper=200, right=250, lower=250
draw.pieslice((200, 200, 250, 250), 0, 90, fill="pink", outline="black")

# Display the result
image.show()

# Save the image
image.save(os.path.join("Manipulated_Image", "love_with_text.jpg"))


# =======================
# 🧾 PIL ImageDraw Function Reference
# =======================
# | Function         | Arguments                                                   | Description                                        |
# |------------------|-------------------------------------------------------------|----------------------------------------------------|
# | draw.line()      | (x1, y1, x2, y2), fill, width                               | Draws a line between two points                    |
# | draw.rectangle() | (left, upper, right, lower), fill, outline, width           | Draws a rectangle                                  |
# | draw.ellipse()   | (left, upper, right, lower), fill, outline, width           | Draws a circle/ellipse                             |
# | draw.polygon()   | [(x1, y1), (x2, y2), ...], fill, outline                    | Draws a polygon with any number of points          |
# | draw.text()      | (x, y), "text", font, fill                                  | Draws text at position                             |
# | draw.arc()       | (left, upper, right, lower), start_angle, end_angle, fill   | Draws only the curved edge                         |
# | draw.chord()     | (left, upper, right, lower), start, end, fill, outline      | Arc with a straight-line between arc ends          |
# | draw.pieslice()  | (left, upper, right, lower), start, end, fill, outline      | Filled wedge like a pie slice                      |
