import numpy as np
from grayscale_conversion import rgb_to_grayscale, matrix_decomposition

# Calculate the probability for each pixel's intensity value
def compute_histogram(grayscale_np_array):

    # Use built-in np function to compute the histogram
    return np.histogram(grayscale_np_array.flatten(), bins=256, range=[0,256])

def test(np_array):

    histogram,_ = compute_histogram(np_array)

    print(f"Histogram for the Image: {histogram}")