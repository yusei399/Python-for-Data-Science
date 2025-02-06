def slice_me(family: list, start: int, end: int) -> list:
    if not all(isinstance(row, list) for row in family):
        raise ValueError("Input must be a 2D list.")
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError("All rows in the 2D list must have the same length.")
    shape = (len(family), row_length)
    print(f"My shape is : {shape}")
    sliced_family = family[start:end]
    new_shape = (len(sliced_family), row_length)
    print(f"My new shape is : {new_shape}")
    return sliced_family


family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
