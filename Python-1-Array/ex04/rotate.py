#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import matplotlib                      # noqa: E402
# matplotlib.use("TkAgg")                # noqa: E402
import matplotlib.pyplot as plt        # noqa: E402
import numpy as np                     # noqa: E402
from load_image import ft_load        # noqa: E402


def show_image(img, cmap="gray"):
    """
    画像を表示する関数

    Args:
        img (numpy.ndarray): 表示する画像データ（NumPy配列）。
        cmap (str, optional): 使用するカラーマップ。デフォルトは "gray"。

    Returns:
        None
    """
    plt.imshow(img, cmap=cmap)
    plt.show()


def crop_image(img_array, x_start=100, x_end=500, y_start=450, y_end=850):
    """
    画像から指定した範囲を切り抜く関数

    Args:
        img_array (numpy.ndarray): 元の画像データ（NumPy配列）。
        x_start (int, optional): 切り抜き開始位置（行方向インデックス）。デフォルトは 100。
        x_end (int, optional): 切り抜き終了位置（行方向インデックス）。デフォルトは 500。
        y_start (int, optional): 切り抜き開始位置（列方向インデックス）。デフォルトは 450。
        y_end (int, optional): 切り抜き終了位置（列方向インデックス）。デフォルトは 850。

    Returns:
        numpy.ndarray: 指定範囲を切り抜いた画像データ。
    """
    cropped_img = img_array[x_start:x_end, y_start:y_end, 0:1]
    return cropped_img


def transpose_image(img_array):
    """
    画像の転置（行と列の入れ替え）を行う関数

    Args:
        img_array (numpy.ndarray): 転置対象の画像データ（NumPy配列）。
                                   ※ この関数はチャネル0のみを用いて転置処理を行います。

    Returns:
        numpy.ndarray: 転置後の画像データ。
    """
    transposed_img = []
    for x in range(img_array.shape[1]):  # 列方向のインデックス
        row = []
        for y in range(img_array.shape[0]):  # 行方向のインデックス
            row.append(img_array[y][x][0])
        transposed_img.append(row)
    return np.array(transposed_img)


def main():
    """
    メイン関数。
    画像を読み込み、指定範囲で切り抜いた後に転置処理を行い、結果を表示します。

    Returns:
        None
    """
    try:
        original_img = load_image("animal.jpeg")
        cropped_img = crop_image(original_img)
        print("切り抜かれた画像の形状:", cropped_img.shape, "または", cropped_img.shape[:2])
        print(cropped_img)
        transposed_img = transpose_image(cropped_img)
        print("転置後の画像の形状:", transposed_img.shape[:2])
        print(transposed_img)
        show_image(transposed_img, cmap="gray")
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
