import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # GUIバックエンドを指定
import matplotlib.pyplot as plt
from load_image import load_image


def invert_colors(array: np.ndarray) -> np.ndarray:
    """
    画像の色を反転させる関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy配列）。

    Returns:
        np.ndarray: 色が反転した画像データ。
    """
    return 255 - array


def extract_red(array: np.ndarray) -> np.ndarray:
    """
    画像から赤チャンネルのみを保持する関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy配列）。

    Returns:
        np.ndarray: 赤チャンネルのみを保持した画像データ。
    """
    array[:, :, 1] = 0  # 緑チャンネルをゼロに
    array[:, :, 2] = 0  # 青チャンネルをゼロに
    return array


def extract_green(array: np.ndarray) -> np.ndarray:
    """
    画像から緑チャンネルのみを保持する関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy配列）。

    Returns:
        np.ndarray: 緑チャンネルのみを保持した画像データ。
    """
    array[:, :, 0] = 0  # 赤チャンネルをゼロに
    array[:, :, 2] = 0  # 青チャンネルをゼロに
    return array


def extract_blue(array: np.ndarray) -> np.ndarray:
    """
    画像から青チャンネルのみを保持する関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy配列）。

    Returns:
        np.ndarray: 青チャンネルのみを保持した画像データ。
    """
    array[:, :, 0] = 0  # 赤チャンネルをゼロに
    array[:, :, 1] = 0  # 緑チャンネルをゼロに
    return array


def convert_to_greyscale(array: np.ndarray) -> np.ndarray:
    """
    画像をグレースケールに変換する関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy配列）。

    Returns:
        np.ndarray: グレースケールに変換された画像データ。
    """
    grey = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) // 3  # RGBの平均値を取得
    grey_img = np.stack((grey, grey, grey), axis=-1)  # RGB形式のグレースケール画像を作成
    return grey_img


if __name__ == "__main__":
    try:
        image_path = 'landscape.jpg'
        array = load_image(image_path)

        # 各フィルタを適用
        inverted_array = invert_colors(array.copy())
        red_array = extract_red(array.copy())
        green_array = extract_green(array.copy())
        blue_array = extract_blue(array.copy())
        grey_array = convert_to_greyscale(array.copy())

        # フィルタ名と適用後の画像をリスト化
        filters = ['Inverted', 'Red', 'Green', 'Blue', 'Greyscale']
        images = [inverted_array, red_array, green_array, blue_array, grey_array]

        # 画像を横に並べて表示
        plt.figure(figsize=(15, 5))
        for i, (img, title) in enumerate(zip(images, filters)):
            plt.subplot(1, 5, i + 1)
            plt.imshow(img)
            plt.title(title)
            plt.axis('off')

        plt.show()

        # Docstringを表示
        print(invert_colors.__doc__)

    except ValueError as e:
        print(e)
