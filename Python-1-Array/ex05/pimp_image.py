import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the image colors."""
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel in the image."""
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    return array


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel in the image."""
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    return array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel in the image."""
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to greyscale."""
    grey = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) // 3
    grey_img = np.stack((grey, grey, grey), axis=-1)
    return grey_img


image_path = 'landscape.jpg'
array = load_image(image_path)

inverted_array = ft_invert(array.copy())
red_array = ft_red(array.copy())
green_array = ft_green(array.copy())
blue_array = ft_blue(array.copy())
grey_array = ft_grey(array.copy())

filters = ['Inverted', 'Red', 'Green', 'Blue', 'Grey']
images = [inverted_array, red_array, green_array, blue_array, grey_array]

for i, (img, title) in enumerate(zip(images, filters)):
    plt.subplot(1, 5, i + 1)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')

plt.show()

print(ft_invert.__doc__)
