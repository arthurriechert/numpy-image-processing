# Used to load an image for a folder
import imageio.v3 as iio

# Used to render image
import matplotlib.pyplot as plt

# Used to check if path exists
import os

# Used to create random array
import numpy as np

def load_image_as_array(path: str):

    # Make sure the path exists
    exists = os.path.exists(path)

    if exists:
        print('Found image.')
        return iio.imread(path)
    else:
        return None

def display_array_image(np_array):
    print(f'Displaying following array\n\033[32m{np_array}\033[0m')
    plt.imshow(np_array)
    plt.show()

image = load_image_as_array('../../images/smiling-guy.jpg')
display_array_image(image)