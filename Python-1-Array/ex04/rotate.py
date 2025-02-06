import matplotlib.pyplot as plt
import numpy as np
from load_image import load_image


def display_image_with_axes(img, cmap):
    plt.imshow(img, cmap=cmap)
    plt.show()


def zoom(img_array, x_start=100, x_end=500, y_start=450, y_end=850):
    zoomed_img = img_array[x_start:x_end, y_start:y_end, 0:1]

    return zoomed_img


def transpose(img_array):
    rotated_img = []
    for x in range(img_array.shape[1]):
        row = []
        for y in range(img_array.shape[0]):
            row.append(img_array[y][x][0])
        rotated_img.append(row)

    return np.array(rotated_img)


def main():
    try:
        original_img = load_image("animal.jpeg")

        zoomed_img = zoom(original_img)
        print("The shape of image is:",
              zoomed_img.shape, "or", zoomed_img.shape[:2])
        print(zoomed_img)
        transposed_img = transpose(zoomed_img)
        print("New shape after Transpose:",
              transposed_img.shape[:2])
        print(transposed_img)

        display_image_with_axes(transposed_img, cmap="gray")

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
