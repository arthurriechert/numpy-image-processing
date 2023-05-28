# Used to load an image for a folder
import imageio.v3 as iio

# Used to render image
import matplotlib.pyplot as plt

# Used to check if path exists
import os

# Used to create random array
import numpy as np

# Convert image into numpy array || Takes path as a string
def load_image_as_array(path: str):

    # Make sure the path exists
    exists = os.path.exists(path)

    if exists:
        print('Found image.')
        return iio.imread(path)
    else:
        return None

# Display image using matplotlib || Takes numpy array
def display_array_image(np_array, cmap):
    plt.imshow(np_array, cmap=cmap)
    plt.show()