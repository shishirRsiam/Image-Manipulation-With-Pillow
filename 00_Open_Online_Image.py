from PIL import Image
import requests
from io import BytesIO

# Image URL
url = 'https://tds-images.thedailystar.net/sites/default/files/styles/very_big_1/public/images/2025/04/19/ncp.jpg'

# Fetch and open the image
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Show or process the image
img.show()

# Close the image file
img.close()