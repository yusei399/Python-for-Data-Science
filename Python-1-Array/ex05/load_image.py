import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    指定されたパスから画像を読み込み、NumPy配列として返す。

    Args:
        path (str): 画像ファイルのパス。空文字列ではなく、JPEGまたはJPG形式の画像である必要がある。

    Returns:
        np.ndarray: 読み込んだ画像のNumPy配列。

    Raises:
        AssertionError: `path` が文字列でない、または空の場合。
        AssertionError: 画像の読み込みに失敗した場合。
        AssertionError: 画像のフォーマットがJPEGまたはJPGでない場合。

    Example:
        >>> img_array = ft_load("example.jpg")
        >>> print(img_array.shape)  # (高さ, 幅, チャネル数)
    """
    assert isinstance(path, str) and len(path) > 0, \
        "パスは空でない文字列である必要があります。"

    img = Image.open(path)

    assert img is not None, "画像を読み込めませんでした。"
    assert img.format in ["JPEG", "JPG"], \
        "対応している画像フォーマットは JPEG または JPG のみです。"

    img_array = np.array(img)

    return img_array


if __name__ == "__main__":
    try:
        image_path = 'landscape.jpg'
        print(ft_load(image_path))
    except ValueError as e:
        print(e)
