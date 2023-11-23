Author: George Somarakis

E-mail: georgesom7@gmail.com

StegaPix Tool:
## Image Embedding Scripts

### Description
These Python scripts demonstrate different techniques for embedding one image within another image, primarily using the Python Imaging Library (PIL).

---

### File Descriptions:

#### `main_1.py`

- Embeds a grayscale image into another grayscale image using the 4 most significant bits from the cover image and the 4 least significant bits from the secret image.

#### `main_2.py`

- Doubles the size of the cover image and embeds the secret image into it by splitting the secret pixel into two parts and distributing it across adjacent pixels of the cover image.

#### `main_3.py`

- Embeds a grayscale image into an RGB image by utilizing the most significant bits of the secret image and merging them with the least significant bits of the cover image for each color channel.

#### `main_4.py`

- Merges two RGB images by splitting the RGB values of both images into 4-bit segments and combining them to create a new image.

---

### Instructions:

- **Setup:**
  - Place the cover images and the secret images in the `Resources` folder as specified in each script.
  - Ensure Python and PIL are installed.

- **Running the Scripts:**
  - Execute each script individually (`python main_1.py`, `python main_2.py`, etc.) to perform the image embedding techniques demonstrated in each file.
  - Output images will be saved in the root directory as specified in each script.

---

Feel free to adjust or expand upon this README file as needed, adding details about prerequisites, usage, or any additional information specific to your use case.
