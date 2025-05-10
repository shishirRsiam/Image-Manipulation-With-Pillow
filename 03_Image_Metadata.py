from PIL import Image, ExifTags

# Open the image
image = Image.open("mee2.jpg")

# Get EXIF metadata (if available)
exif_data = image.getexif()

# Decode EXIF tag names and print them
for tag_id, value in exif_data.items():
    tag = ExifTags.TAGS.get(tag_id, tag_id)
    print(f"{tag:25}: {value}")
