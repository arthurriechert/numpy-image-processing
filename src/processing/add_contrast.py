# Main library for manipulating image matrix representations
import numpy as np

# Takes 3D, RGB array and does min-max stretch || Takes numpy array
# Check README.md for more info
# g(x, y)=(f(x,y)-min)/(max-min))*No. of the intensity level
def rgb_min_max_linear_stretch(R, G, B):

    print(f'Input arrays are: \nR:{R.shape}\nG:{G.shape}\nB:{B.shape}\nHere are the input arrays:\n\033[32m{np.transpose(np.array([R, G, B], dtype=np.uint8), (1, 2, 0))}\033[0m')

    # Find minimum and maximum intensity values
    min_R, max_R = np.min(R), np.max(R)
    min_G, max_G = np.min(G), np.max(G)
    min_B, max_B = np.min(B), np.max(B)
    print(f'Min is {min_R}\nMax is {max_R}')

    # Use numpy built-in broadcasting to apply the formula
    R = ((R - min_R) / (max_R - min_R)) * 255
    G = ((G - min_G) / (max_G - min_G)) * 255
    B = ((B - min_B) / (max_B - min_B)) * 255

    # print(f'Stretched arrays are: \nR:{tmp_R}\nG:{tmp_G}\nB:{tmp_B}')

    # Transpose to ensure correct shape and apply uint8 to avoid incorrect truncation
    return np.transpose(np.array([R, G, B], dtype=np.uint8), (1, 2, 0))