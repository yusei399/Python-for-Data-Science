from math import ceil, sqrt
from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    与えられた数値群から、要求された統計量を計算して出力します。

    *args:
        数値（int または float）が可変長で渡される。
    **kwargs:
        統計量の指定。値として以下のいずれかを指定可能:
            "mean"      : 平均
            "median"    : 中央値
            "quartile"  : 第一四分位数と第三四分位数（リスト形式で出力）
            "std"       : 標準偏差
            "var"       : 分散

    エラー処理:
        - 数値が一つも提供されない場合、指定された統計量の数だけ "ERROR" を出力する。
        - 数値以外が含まれている場合も同様に "ERROR" を出力する。
        - 有効な統計量指定でない場合は、出力しない。
    """
    numbers = []
    for a in args:
        try:
            num = float(a)
            numbers.append(num)
        except (ValueError, TypeError):
            for _ in kwargs:
                print("ERROR")
            return

    if not numbers:
        for _ in kwargs:
            print("ERROR")
        return

    numbers.sort()
    n = len(numbers)

    # 平均の計算
    mean_val = sum(numbers) / n

    # 中央値の計算
    if n % 2 == 1:
        median_val = numbers[n // 2]
    else:
        median_val = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    rank_q1 = ceil(0.25 * n)
    rank_q3 = ceil(0.75 * n)
    q1 = numbers[rank_q1 - 1]
    q3 = numbers[rank_q3 - 1]
    quartile_val = [float(q1), float(q3)]

    # 分散と標準偏差の計算
    var_val = sum((x - mean_val) ** 2 for x in numbers) / n
    std_val = sqrt(var_val)

    allowed = {"mean", "median", "quartile", "std", "var"}

    # 統計量の出力
    for stat in kwargs.values():
        if stat not in allowed:
            continue
        if stat == "mean":
            print(f"mean : {mean_val}")
        elif stat == "median":
            if median_val.is_integer():
                print(f"median : {int(median_val)}")
            else:
                print(f"median : {median_val}")
        elif stat == "quartile":
            print(f"quartile : {quartile_val}")
        elif stat == "std":
            print(f"std : {std_val}")
        elif stat == "var":
            print(f"var : {var_val}")
