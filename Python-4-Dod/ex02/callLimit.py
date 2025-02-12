def callLimit(limit: int):
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

