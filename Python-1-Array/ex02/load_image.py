from PIL import Image
import numpy as np

def load_image(image_path: str):
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        
        print(f"The shape of image is: {img_array.shape}")
        
        print(img_array[:1, :5, :])

        return img

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_path = 'landscape.jpg'
    load_image(image_path)
