def callLimit(limit: int):
    """関数の呼び出し回数を制限するデコレーター。

    引数:
        limit (int): 最大呼び出し回数。

    戻り値:
        callable: 指定回数を超えた場合にエラーを出すデコレーター。
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print("Error: {} call too many times".format(function))
        return limit_function
    return callLimiter
