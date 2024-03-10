def ft_filter(f1, iterable):
    """
    Apply a function to each element of the iterable, returning only the elements for which the function returns True.
    If the function is None, return the elements that are true.
    """
    if f1:
        return [i for i in iterable if f1(i)]
    return [i for i in iterable if i]

def main():
    test_cases = [
        (None, [0, 1, False, True, [], [1], '', 'hello'], "Boolean evaluation"),
        (lambda x: x > 0, range(-5, 6), "Filtering positive numbers"),
        (lambda x: x % 2 == 0, range(10), "Filtering even numbers"),
        (None, [], "Empty iterable"),
        (None, [None, 0, '', {}, [], 1, 'a', [0]], "None function with mixed values")
    ]

    for func, iterable, description in test_cases:
        try:
            result_custom = ft_filter(func, iterable)
            result_builtin = list(filter(func, iterable))
            assert result_custom == result_builtin, f"Failed at {description}"
            print(f"Passed: {description}")
        except Exception as e:
            print(f"Failed: {description} with error {e}")

if __name__ == "__main__":
    main()
