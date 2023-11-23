from PIL import Image

# Open the images
cover_image = Image.open('Resources/Cover_Image.bmp')
secret_image = Image.open('Resources/ID_200x100GS.bmp')

# Ensure images are in 8-bit grayscale
cover_image = cover_image.convert('L')
secret_image = secret_image.convert('L')

# Double the cover image by copying it
cover_image = cover_image.resize((cover_image.size[0]*2, cover_image.size[1]*2))

# Get the pixel data
cover_pixels = cover_image.load()
secret_pixels = secret_image.load()

# Create a new image to store the result
result_image = Image.new('L', cover_image.size)
result_pixels = result_image.load()

# Iterate over each pixel in the secret image
for i in range(secret_image.width):
    for j in range(secret_image.height):
        # Get the pixel value from the secret image
        secret_pixel = secret_pixels[i, j]

        # Retrieve the most significant bits (2 bits) from the secret pixel
        msb = (secret_pixel & 0xC0) >> 6

        # Embed these bits into the cover image pixels
        cover_pixels[i*2, j*2] = (cover_pixels[i*2, j*2] & 0xFC) | msb

        # Check if there's enough space in the cover image to embed more bits
        if i*2+1 < cover_image.width and j*2+1 < cover_image.height:
            # Retrieve the next bit (LSB) from the secret pixel
            lsb = (secret_pixel & 0x20) >> 5

            # Embed this bit into the cover image pixels
            cover_pixels[i*2+1, j*2+1] = (cover_pixels[i*2+1, j*2+1] & 0xFE) | lsb

# Save the modified cover image with the embedded secret
cover_image.save('Result_image_2.bmp')
