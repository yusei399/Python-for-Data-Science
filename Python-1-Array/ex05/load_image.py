from PIL import Image
import numpy as np

def ft_load(image_path: str) -> np.ndarray:
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        
        print(f"The shape of image is: {img_array.shape}")
        
        print(img_array[:1, :5, :])

        return img_array

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Path to the image
if __name__ == "__main__":
    image_path = 'landscape.jpg'
    ft_load(image_path)
