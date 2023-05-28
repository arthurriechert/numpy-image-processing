import processing.load_image as pr
import processing.gray_scale_conversion as gsc

if __name__ == "__main__":
    image_array = pr.load_image_as_array('../images/smiling-guy.jpg')
    R, G, B = gsc.matrix_decomposition(image_array)
    image_array = gsc.convert_RGB_to_grayscale(R, G, B)
    print(f'Gray-scaled matrix is:\n{image_array}')
    pr.display_array_image(image_array, 'gray')