# Convert an RGB matrix into individual components || Takes numpy array
def matrix_decomposition(np_array):
    R = np_array[:,:,0]
    G = np_array[:,:,1]
    B = np_array[:,:,2]
    return R, G, B

# Converts R, G, B to grayscale || R, G, B are numpy arrays
def rgb_to_grayscale(R, G, B):
    R = R * 0.299
    G = G * 0.587
    B = B * 0.114
    
    # Combine into single array
    grayscale = R + G + B

    return grayscale