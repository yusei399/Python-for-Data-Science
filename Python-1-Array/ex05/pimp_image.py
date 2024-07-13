import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def ft_invert(array: np.ndarray) -> np.ndarray:
    return 255 - array

def ft_red(array: np.ndarray) -> np.ndarray:
    array[:, :, 1] = 0 
    array[:, :, 2] = 0
    return array

def ft_green(array: np.ndarray) -> np.ndarray:
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    return array

def ft_blue(array: np.ndarray) -> np.ndarray:
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return array

def ft_grey(array: np.ndarray) -> np.ndarray:
    grey = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) // 3
    grey_img = np.stack((grey, grey, grey), axis=-1)
    return grey_img

image_path = 'landscape.jpg'
array = ft_load(image_path)

inverted_array = ft_invert(array.copy())
red_array = ft_red(array.copy())
green_array = ft_green(array.copy())
blue_array = ft_blue(array.copy())
grey_array = ft_grey(array.copy())

filters = ['Inverted', 'Red', 'Green', 'Blue', 'Grey']
images = [inverted_array, red_array, green_array, blue_array, grey_array]

for i, (img, title) in enumerate(zip(images, filters)):
    plt.subplot(1, 5, i+1)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')

plt.show()

print(ft_invert.__doc__)
