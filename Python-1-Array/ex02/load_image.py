from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    assert isinstance(path, str) and len(path) > 0, \
        "The path must be a string."

    img = Image.open(path)

    assert img is not None, "The image could not be loaded."
    assert img.format in ["JPEG", "JPG"], \
        "The image format is not supported."

    img_array = np.array(img)

    return img_array


if __name__ == "__main__":
    image_path = 'landscape.jpg'
    ft_load(image_path)
