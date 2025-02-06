import matplotlib.pyplot as plt
from load_image import ft_load


def display_image_with_axes(img, cmap):
    plt.imshow(img, cmap=cmap)
    plt.show()


def zoom(img_array, x_start=100, x_end=500, y_start=450, y_end=850):
    zoomed_img = img_array[x_start:x_end, y_start:y_end, 0:1]

    return zoomed_img


def main():
    try:
        original_img = ft_load("animal.jpeg")
        print("The shape of image is:", original_img.shape)
        print(original_img)

        zoomed_img = zoom(original_img)
        print("New shape after slicing:",
              zoomed_img.shape, "or", zoomed_img.shape[:2])
        print(zoomed_img)

        display_image_with_axes(zoomed_img, cmap="gray")

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
