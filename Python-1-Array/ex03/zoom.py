#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib                      # noqa: E402
matplotlib.use("TkAgg")                # noqa: E402
import matplotlib.pyplot as plt        # noqa: E402
from load_image import load_image      # noqa: E402


def show_image(img, cmap="gray"):
    """
    画像を表示する。

    Args:
        img (numpy.ndarray): 表示する画像データ（NumPy 配列）。
        cmap (str, optional): カラーマップ（デフォルトは "gray"）。

    Returns:
        None
    """
    plt.imshow(img, cmap=cmap)
    plt.show()


def crop_image(img_array, x_start=100, x_end=500, y_start=450, y_end=850):
    """
    指定された範囲で画像を切り抜く。

    Args:
        img_array (numpy.ndarray): 元の画像データ（NumPy 配列）。
        x_start (int, optional): 切り抜き開始位置（X軸方向）。デフォルトは 100。
        x_end (int, optional): 切り抜き終了位置（X軸方向）。デフォルトは 500。
        y_start (int, optional): 切り抜き開始位置（Y軸方向）。デフォルトは 450。
        y_end (int, optional): 切り抜き終了位置（Y軸方向）。デフォルトは 850。

    Returns:
        numpy.ndarray: 指定範囲を切り抜いた新しい画像データ。
    """
    zoom_image = img_array[x_start:x_end, y_start:y_end, 0:1]
    return zoom_image


def main():
    """
    画像を読み込み、サイズを表示し、切り抜いた後に表示する。

    Raises:
        AssertionError: `load_image` で発生する可能性のあるアサーションエラー。
        Exception: その他の予期しない例外。

    Returns:
        None
    """
    try:
        original_img = load_image("animal.jpeg")
        print("The shape of image is:", original_img.shape)
        print(original_img)

        zoom_image = crop_image(original_img)
        print("New shape after slicing:",
              zoom_image.shape, "or", zoom_image.shape[:2])
        print(zoom_image)

        show_image(zoom_image, cmap="gray")

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
