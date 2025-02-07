from typing import List, Union

def give_bmi(
    height: List[Union[int, float]],
    weight: List[Union[int, float]]
) -> List[float]:
    if not all(isinstance(h, (int, float)) for h in height):
        raise ValueError("All height values must be integers or floats.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("All weight values must be integers or floats.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    bmi = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("Height values must be greater than zero.")
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(
    bmi: List[Union[int, float]],
    limit: int
) -> List[bool]:
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("All BMI values must be integers or floats.")
    if not isinstance(limit, int):
        raise ValueError("Limit must be an integer.")

    return [b > limit for b in bmi]


if __name__ == "__main__":
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as error:
        print(error)

