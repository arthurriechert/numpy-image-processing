import numpy as np
from grayscale_conversion import rgb_to_grayscale, matrix_decomposition

# Calculate the probability for each pixel's intensity value
def compute_histogram(np_array):

    R, G, B = matrix_decomposition(np_array)

    grayscale = rgb_to_grayscale(R, G, B)

    # Use bincount to compute the histogram
    return np.bincount(grayscale.flatten(), minlength=256)