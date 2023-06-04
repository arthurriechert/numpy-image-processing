import processing.load_image as pr
import processing.grayscale_conversion as gsc
import processing.negative_conversion as nc
import processing.add_contrast as ac
import processing.histogram_equalization as he

if __name__ == "__main__":
    image_array = pr.load_image_as_array('../images/smiling-guy.jpg')
    R, G, B = gsc.matrix_decomposition(image_array)
    # image_array = gsc.rgb_to_grayscale(R, G, B)
    image_array = ac.rgb_min_max_linear_stretch(R, G, B)
    # image_array = nc.rgb_to_negative(image_array)
    print(f'Stretched matrix is:\n{image_array}')
    print(f'Shape is {image_array.shape}')
    pr.display_array_image(image_array)