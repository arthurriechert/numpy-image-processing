import processing.load_image as pr

if __name__ == "__main__":
    image = pr.load_image_as_array('../images/smiling-guy.jpg')
    pr.display_array_image(image)