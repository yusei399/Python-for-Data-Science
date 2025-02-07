def slice_me(family: list, start: int, end: int) -> list:
    """
    2次元リスト（リストのリスト）をスライスして部分リストを取得する。

    Args:
        family (list): 2Dリスト（リストのリスト）。すべての行の長さが同じである必要がある。
        start (int): スライスの開始インデックス（リストの開始位置）。
        end (int): スライスの終了インデックス（リストの終了位置）。

    Returns:
        list: 指定した範囲のスライス後の2Dリスト。

    Raises:
        ValueError: `family` がリストでない場合。
        ValueError: `family` の各要素がリストでない場合（2Dリストでない場合）。
        ValueError: `family` 内のすべての行の長さが一致しない場合。
        ValueError: `start` または `end` が整数でない場合。
    """
    if not isinstance(family, list):
        raise ValueError("Input must be a list representing a 2D array.")

    if family:
        if not all(isinstance(row, list) for row in family):
            raise ValueError("Input must be a 2D list (a list of lists).")
        first_row_length = len(family[0])
        for i, row in enumerate(family):
            if len(row) != first_row_length:
                raise ValueError("All rows in the 2D list \
                must have the same length.")
    else:
        first_row_length = 0

    original_shape = (len(family), first_row_length)
    print(f"My shape is : {original_shape}")

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end parameters must be integers.")

    sliced_family = family[start:end]
    new_shape = (len(sliced_family), first_row_length)
    print(f"My new shape is : {new_shape}")

    return sliced_family


if __name__ == "__main__":
    try:
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except ValueError as e:
        print(e)
