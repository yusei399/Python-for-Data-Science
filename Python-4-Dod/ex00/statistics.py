from typing import Any
import math

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for key, value in kwargs.items():
        if key == "mean":
            print(f"mean: {sum(args) / len(args)}")
        elif key == "median":
            print(f"median: {sorted(args)[len(args) // 2]}")
        elif key == "quartile":
            print(f"quartile: {sorted(args)[len(args) // 4]}")
        elif key == "std":
            print(f"std: {math.sqrt(sum((x - sum(args) / len(args)) ** 2 for x in args) / len(args))}")
        elif key == "var":
            print(f"var: {sum((x - sum(args) / len(args)) ** 2 for x in args) / len(args)}")
        else:
            print("ERROR")
