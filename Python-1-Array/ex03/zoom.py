from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image

def zoom_image(img, zoom_size=(400, 400)):
    try:
        width, height = img.size
        left = (width - zoom_size[0]) / 2
        top = (height - zoom_size[1]) / 2
        right = (width + zoom_size[0]) / 2
        bottom = (height + zoom_size[1]) / 2

        zoomed_img = img.crop((left, top, right, bottom))
        zoomed_img_array = np.array(zoomed_img.convert('L'))

        print(f"New shape after slicing: {zoomed_img_array.shape}")

        print(zoomed_img_array[:1, :5])

        plt.imshow(zoomed_img_array, cmap='gray')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Zoomed Image')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = 'animal.jpeg'
    img = load_image(image_path)
    if img:
        zoom_image(img)
