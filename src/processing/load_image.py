# Used to load an image for a folder
import imageio.v3 as iio

# Used to render image
import matplotlib.pyplot as plt

# Used to check if path exists

def load_image_as_array(path: str):

    return iio.imread(path)

def display_array_image(np_array):
    plt.imshow(np_array)

image = load_image_as_array('../../images/smiling-guy.jpg')
display_array_image(image)