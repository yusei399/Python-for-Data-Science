from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image

def rotate_image(img, square_size=(400, 400)):
    try:
        width, height = img.size
        left = (width - square_size[0]) / 2
        top = (height - square_size[1]) / 2
        right = (width + square_size[0]) / 2
        bottom = (height + square_size[1]) / 2

        square_img = img.crop((left, top, right, bottom))
        square_img_array = np.array(square_img.convert('L'))

        print(f"The shape of image is: {square_img_array.shape}")

        print(square_img_array[:1, :5])

        transposed_img_array = np.transpose(square_img_array)

        print(f"New shape after Transpose: {transposed_img_array.shape}")

        print(transposed_img_array[:1, :5])

        plt.imshow(transposed_img_array, cmap='gray')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Transposed Image')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = 'animal.jpeg'
    img = load_image(image_path)
    if img:
        rotate_image(img)
