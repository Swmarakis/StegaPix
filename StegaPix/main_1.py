#Author: George Somarakis

from PIL import Image

# Open the images
cover_image = Image.open('Resources/Cover_Image.bmp')
secret_image = Image.open('Resources/ID_200x100GS.bmp')

# Ensure images are in 8-bit grayscale
cover_image = cover_image.convert('L')
secret_image = secret_image.convert('L')

# Get the pixel data
cover_pixels = cover_image.load()
secret_pixels = secret_image.load()

# Create a new image to store the result
result_image = Image.new('L', cover_image.size)
result_pixels = result_image.load()

# Iterate over each pixel
for i in range(cover_image.width):
    for j in range(cover_image.height):
        # Get the 4 most significant bits from the cover image
        cover_bits = cover_pixels[i, j] & 0xF0
        # Get the 4 least significant bits from the secret image
        secret_bits = secret_pixels[i, j] >> 4
        # Combine the bits
        result_pixels[i, j] = cover_bits | secret_bits

# Save the result
result_image.save('Result_image_1.bmp')
