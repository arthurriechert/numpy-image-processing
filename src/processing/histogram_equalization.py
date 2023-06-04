import numpy as np

# Count the number of times each intensity value appears
def compute_histogram(grayscale_np_array):

    # Use built-in np function to compute the histogram
    return np.histogram(grayscale_np_array.flatten(), bins=256, range=[0,256])

# Calculate the probabilites for each intensity value
def compute_probabilties(histogram):

    pixel_count = np.sum(histogram)

    # Normalize
    return histogram / pixel_count

def compute_cdf(probabilities):

    return np.cumsum(probabilities)

# Apply the histogram
def equalize(image_array, cdf_array):
    
    # Convert elements to integer indices
    indices = image_array.astype(np.uint32)

    # Create mapping for original to new values
    intensity_mapping = np.uint8(255 * cdf_array)

    # Apply transformation
    return intensity_mapping[indices]

def test(np_array):

    histogram,_ = compute_histogram(np_array)

    probabilties = compute_probabilties(histogram)

    cdf = compute_cdf(probabilties)

    equalized_image = equalize(np_array, cdf)

    print(f"""
        ###### HISTOGRAM ######
          
        {histogram}

        
        ###### PROBABILTIIES ######

        {probabilties}

        ###### CDF ######

        {cdf}

        
        ###### NEW IMAGE ARRAY ######

        {equalized_image}
        
        """)