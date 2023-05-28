import processing.load_image as pr
import processing.grayscale_conversion as gsc
import processing.negative_conversion as nc

if __name__ == "__main__":
    image_array = pr.load_image_as_array('../images/smiling-guy.jpg')
    # R, G, B = gsc.matrix_decomposition(image_array)
    # image_array = gsc.rgb_to_grayscale(R, G, B)
    image_array = nc.rgb_to_negative(image_array)
    print(f'Negative matrix is:\n{image_array}')
    pr.display_array_image(image_array)