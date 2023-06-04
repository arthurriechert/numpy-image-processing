import numpy as np
from grayscale_conversion import rgb_to_grayscale, matrix_decomposition

# Calculate the probability for each pixel's intensity value
def compute_histogram(np_array):

    R, G, B = matrix_decomposition(np_array)

    grayscale = rgb_to_grayscale(R, G, B)

    # Use built-in np function to compute the histogram
    return np.histogram(grayscale.flatten(), bins=256, range=[0,256])

def test(np_array):

    histogram,_ = compute_histogram(np_array)

    print(f"Histogram for the Image: {histogram}")