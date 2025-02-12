#!/usr/bin/env python3
class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        2つのベクトルのドット積（内積）を計算し、その結果を表示する。
        例: [a, b, c] と [x, y, z] のドット積は a*x + b*y + c*z
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print("Dot product is: {}".format(result))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        2つのベクトルを要素ごとに加算し、結果のベクトルを表示する。
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is : {}".format(result))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        第2のベクトルを第1のベクトルから要素ごとに減算し、結果のベクトルを表示する。
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is: {}".format(result))
