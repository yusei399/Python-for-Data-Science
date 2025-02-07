import numpy as np
# import matplotlib
# matplotlib.use("TkAgg")  # GUIバックエンドを指定
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    画像の色を反転させる関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy 配列）。

    Returns:
        np.ndarray: 色が反転した画像データ。
    """
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    画像から赤チャンネルのみを保持する関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy 配列）。

    Returns:
        np.ndarray: 赤チャンネルのみを保持した画像データ。
    """
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    return array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    画像から緑チャンネルのみを保持する関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy 配列）。

    Returns:
        np.ndarray: 緑チャンネルのみを保持した画像データ。
    """
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    return array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    画像から青チャンネルのみを保持する関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy 配列）。

    Returns:
        np.ndarray: 青チャンネルのみを保持した画像データ。
    """
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    画像をグレースケールに変換する関数。

    Args:
        array (np.ndarray): 元の画像データ（NumPy 配列）。

    Returns:
        np.ndarray: グレースケールに変換された画像データ。
    """
    grey = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) // 3  # RGBの平均値を取得
    grey_img = np.stack((grey, grey, grey), axis=-1)  # RGB 形式のグレースケール画像を作成
    return grey_img


if __name__ == "__main__":
    try:
        image_path = 'landscape.jpg'
        array = load_image(image_path)

        # 各フィルタを適用
        inverted_array = ft_invert(array.copy())
        red_array = ft_red(array.copy())
        green_array = ft_green(array.copy())
        blue_array = ft_blue(array.copy())
        grey_array = ft_grey(array.copy())

        # フィルタ名と適用後の画像をリスト化
        filters = ['Inverted', 'Red', 'Green', 'Blue', 'Grey']
        images = [inverted_array, red_array, green_array, blue_array, grey_array]

        # 画像を横に並べて表示
        plt.figure(figsize=(15, 5))
        for i, (img, title) in enumerate(zip(images, filters)):
            plt.subplot(1, 5, i + 1)
            plt.imshow(img)
            plt.title(title)
            plt.axis('off')

        plt.show()

        
        print(ft_invert.__doc__)

    except ValueError as e:
        print(e)
