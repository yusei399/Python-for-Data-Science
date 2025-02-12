class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object):
        """ベクトルの各要素にスカラー値を加え、結果を表示する。"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object):
        """ベクトルの各要素にスカラー値を掛け、結果を表示する。"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object):
        """ベクトルの各要素からスカラー値を引き、結果を表示する。"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object):
        """ベクトルの各要素をスカラー値で割り、結果を表示する。"""
        try:
            if object == 0:
                raise ZeroDivisionError("ゼロによる除算は許可されていません。")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return [x for x in self.vector]
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
