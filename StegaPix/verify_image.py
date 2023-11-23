from PIL import Image

def embed_secret(cover_image_path, secret_image_path):
    # Open the cover image and the secret image
    cover_image = Image.open(cover_image_path).convert('L')
    secret_image = Image.open(secret_image_path).convert('L')

    # Double the cover image by copying it
    cover_image = cover_image.resize((cover_image.size[0] * 2, cover_image.size[1] * 2))
    cover_pixels = cover_image.load()
    secret_pixels = secret_image.load()

    # Iterate over each pixel in the secret image and embed it in the cover image
    for i in range(secret_image.width):
        for j in range(secret_image.height):
            # Retrieve the pixel value from the secret image
            secret_pixel = secret_pixels[i, j]

            # Retrieve the most significant bits (2 bits) from the secret pixel
            msb = (secret_pixel & 0xC0) >> 6

            # Embed these bits into the cover image pixels
            cover_pixels[i * 2, j * 2] = (cover_pixels[i * 2, j * 2] & 0xFC) | msb

            # Check if there's enough space in the cover image to embed more bits
            if i * 2 + 1 < cover_image.width and j * 2 + 1 < cover_image.height:
                # Retrieve the next bit (LSB) from the secret pixel
                lsb = (secret_pixel & 0x20) >> 5

                # Embed this bit into the cover image pixels
                cover_pixels[i * 2 + 1, j * 2 + 1] = (cover_pixels[i * 2 + 1, j * 2 + 1] & 0xFE) | lsb

    # Save the modified cover image with the embedded secret
    cover_image.save('Modified_Cover_Image.bmp')

    # Return the modified cover image and the secret image
    return cover_image, secret_image

def extract_secret(modified_cover_image, secret_image):
    modified_cover_pixels = modified_cover_image.load()
    secret_pixels = secret_image.load()

    # Create a blank image to store the extracted secret image
    extracted_secret_image = Image.new('L', (secret_image.width, secret_image.height))
    extracted_pixels = extracted_secret_image.load()

    # Iterate over each pixel in the secret image
    for i in range(secret_image.width):
        for j in range(secret_image.height):
            # Retrieve the embedded bits from the modified cover image
            msb = (modified_cover_pixels[i * 2, j * 2] & 0x03) << 6
            lsb = (modified_cover_pixels[i * 2 + 1, j * 2 + 1] & 0x01) << 5

            # Combine the bits to reconstruct the original pixel value
            pixel_value = msb | lsb
            extracted_pixels[i, j] = pixel_value

    # Save the extracted secret image
    extracted_secret_image.save('Extracted_Secret_Image.bmp')

    return extracted_secret_image

def verify_extraction(original_secret_image_path, extracted_secret_image_path):
    # Open the original secret image and the extracted secret image
    original_secret_image = Image.open(original_secret_image_path)
    extracted_secret_image = Image.open(extracted_secret_image_path)

    # Compare the two images pixel by pixel and calculate PSNR
    mse = 0
    for x in range(original_secret_image.width):
        for y in range(original_secret_image.height):
            mse += (original_secret_image.getpixel((x, y)) - extracted_secret_image.getpixel((x, y))) ** 2
    mse /= float(original_secret_image.width * original_secret_image.height)
    psnr = 20 * (255 ** 2 / mse) ** 0.5

    return psnr

# Paths to the images
cover_image_path = 'Resources/Cover_Image.bmp'
secret_image_path = 'Resources/ID_200x100GS.bmp'

# Embed the secret into the cover image and retrieve modified cover and secret images
modified_cover_image, secret_image = embed_secret(cover_image_path, secret_image_path)

# Extract the secret from the modified cover image
extracted_image = extract_secret(modified_cover_image, secret_image)

# Verify the extraction process
psnr = verify_extraction(secret_image_path, 'Extracted_Secret_Image.bmp')

print(f"PSNR: {psnr}")
