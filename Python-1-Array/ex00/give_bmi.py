from typing import List, Union


def give_bmi(
    height: List[Union[int, float]],
    weight: List[Union[int, float]]
) -> List[float]:
    """
    身長と体重のリストから BMI（ボディマス指数）を計算する。

    Args:
        height (List[Union[int, float]]): 身長（メートル単位）のリスト。
                                          すべての要素は整数または浮動小数点数である必要があります。
        weight (List[Union[int, float]]): 体重（キログラム単位）のリスト。
                                          すべての要素は整数または浮動小数点数である必要があります。

    Returns:
        List[float]: 各身長・体重ペアに対応する BMI のリスト。
                     BMI は「体重 ÷ (身長の2乗)」で計算されます。

    Raises:
        ValueError: 身長または体重のリストに数値以外の値が含まれている場合。
        ValueError: 身長と体重のリストの長さが一致しない場合。
        ValueError: 身長の値が 0 以下である場合。
    """
    if not all(isinstance(h, (int, float)) for h in height):
        raise ValueError("身長はすべて整数または浮動小数点数である必要があります。")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("体重はすべて整数または浮動小数点数である必要があります。")
    if len(height) != len(weight):
        raise ValueError("身長と体重のリストの長さが一致している必要があります。")

    bmi = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("身長の値は 0 より大きくなければなりません。")
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(
    bmi: List[Union[int, float]],
    limit: int
) -> List[bool]:
    """
    BMI のリストに対して制限値を適用し、各 BMI が制限を超えているかを判定する。

    Args:
        bmi (List[Union[int, float]]): BMI のリスト。
                                       すべての要素は整数または浮動小数点数である必要があります。
        limit (int): 比較対象となる制限値（整数）。

    Returns:
        List[bool]: 各 BMI が制限値を超えている場合は `True`、超えていない場合は `False` を返すリスト。

    Raises:
        ValueError: BMI のリストに数値以外の値が含まれている場合。
        ValueError: 制限値が整数でない場合。
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("BMI のリストはすべて整数または浮動小数点数である必要があります。")
    if not isinstance(limit, int):
        raise ValueError("制限値は整数である必要があります。")

    return [b > limit for b in bmi]


if __name__ == "__main__":
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
        # print(apply_limit.__doc__)
    except ValueError as error:
        print(error)
