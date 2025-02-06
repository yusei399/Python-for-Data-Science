#!/usr/bin/env python3
class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the dot product of two vectors and prints the result.
        Example: dot product of [a, b, c] and [x, y, z] is a*x + b*y + c*z.
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print("Dot product is: {}".format(result))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise and prints the resulting vector.
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is : {}".format(result))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first element-wise and prints the resulting vector.
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is: {}".format(result))
