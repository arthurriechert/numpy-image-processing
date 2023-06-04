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

def test(np_array):

    histogram,_ = compute_histogram(np_array)

    probabilties = compute_probabilties(histogram)

    cdf = compute_cdf(probabilties)

    print(f"""
        ###### HISTOGRAM ######
          
        {histogram}

        
        ###### PROBABILTIIES ######

        {probabilties}

        ###### CDF ######

        {cdf}
        """)