def square(x: int | float) -> int | float:
    return x ** 2

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
        count = 0
        try:
            assert isinstance(x, (int, float)), "x must be int or float"
            assert callable(function), "function must be callable"

            def inner() -> float:

                nonlocal x
                nonlocal count

                x = function(x)
                count += 1

                return x

            return inner
        except AssertionError as e:
            print("AssertionError:", e)
            return None