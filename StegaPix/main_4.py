#Author: George Somarakis

from PIL import Image

# Define the black pixel
BLACK_PIXEL = (0, 0, 0)

# Load the two images
image1 = Image.open('Resources/Cover_image_rgb.bmp').convert('RGB')
image2 = Image.open('Resources/ID_200x100GS.bmp').convert('RGB')

# Check if image2 is smaller than image1
if image2.size[0] > image1.size[0] or image2.size[1] > image1.size[1]:
    raise ValueError('Image 2 should be smaller than Image 1!')

# Load the pixel maps of the two images
map1 = image1.load()
map2 = image2.load()

# Create a new image with the same mode and size as image1
new_image = Image.new(image1.mode, image1.size)
new_map = new_image.load()

# Iterate over the pixels of image1
for i in range(image1.size[0]):
    for j in range(image1.size[1]):
        # Check if the current pixel is within the bounds of image2
        is_valid = i < image2.size[0] and j < image2.size[1]
        # Get the RGB values of the current pixel in image1
        rgb1 = map1[i, j]
        # Get the RGB values of the current pixel in image2 if it is valid, otherwise use a black pixel
        rgb2 = map2[i, j] if is_valid else BLACK_PIXEL
        # Merge the two RGB values
        r1, g1, b1 = [f'{value:08b}' for value in rgb1]
        r2, g2, b2 = [f'{value:08b}' for value in rgb2]
        rgb = r1[:4] + r2[:4], g1[:4] + g2[:4], b1[:4] + b2[:4]
        new_map[i, j] = tuple(int(value, 2) for value in rgb)

# Save the new image
new_image.save('Result_image_rgb_4.bmp')
