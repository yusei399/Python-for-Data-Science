def square(x: int | float) -> int | float:
    """与えられた数の二乗を返します。

    引数:
        x (int | float): 二乗する数値。

    戻り値:
        int | float: 入力値の二乗。
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """自身の値を指数として累乗した結果を返します。

    引数:
        x (int | float): 底となる数値。

    戻り値:
        int | float: x を x 乗した結果。
    """
    return x ** x


def outer(x: int | float, function: callable) -> object | None:
    """指定された関数を x に繰り返し適用する関数を返します。

    引数:
        x (int | float): 初期値。
        function (callable): x に適用する関数。

    戻り値:
        object | None: `function` を x に繰り返し適用する関数、またはエラー時には None。
    """
    count = 0
    try:
        if not isinstance(x, (int, float)):
            raise TypeError("x は int または float でなければなりません")
        if not callable(function):
            raise TypeError("function は呼び出し可能でなければなりません")

        def inner() -> float:
            """関数を x に適用し、更新された値を返します。"""
            nonlocal x, count
            x = function(x)
            count += 1
            return x

        return inner
    except TypeError as e:
        print("TypeError:", e)
        return None
