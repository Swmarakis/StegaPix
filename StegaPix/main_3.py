from PIL import Image

# Open the images
cover_image = Image.open('Resources/Cover_image_rgb.bmp')
secret_image = Image.open('Resources/ID_200x100GS.bmp')

# Ensure secret image is in 8-bit grayscale
secret_image = secret_image.convert('L')

# Convert cover image to RGB mode
cover_image = cover_image.convert('RGB')

# Resize secret image to match cover image dimensions
secret_image = secret_image.resize(cover_image.size)

# Get the pixel data
cover_pixels = cover_image.load()
secret_pixels = secret_image.load()

# Create a new image to store the result
result_image = Image.new('RGB', cover_image.size)
result_pixels = result_image.load()

# Iterate over each pixel in the cover image
for i in range(cover_image.width):
    for j in range(cover_image.height):
        # Get RGB values from the cover image
        cover_r, cover_g, cover_b = cover_pixels[i, j]

        # Get the corresponding pixel value from the secret image
        secret_value = secret_pixels[i, j]

        # Extract the 6 most significant bits from the secret image
        secret_bits_r = (secret_value & 0xFC) >> 2
        secret_bits_g = (secret_value & 0xFC) >> 2
        secret_bits_b = (secret_value & 0xFC) >> 2

        # Combine the 2 least significant bits from the cover image with the 6 most significant bits from the secret image
        result_pixels[i, j] = (
            (cover_r & 0xFC) | secret_bits_r,
            (cover_g & 0xFC) | secret_bits_g,
            (cover_b & 0xFC) | secret_bits_b
        )

# Save the result
result_image.save('Result_image_rgb.bmp')
