from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon 家を表現するクラス。

    Attributes:
        family_name (str): 家族名 "Baratheon" を保持します。
        eyes (str): 目の色。初期値は "brown" です。
        hairs (str): 髪の色。初期値は "dark" です。
    """

    def __init__(self, first_name, is_alive=True):
        """
        Baratheon クラスのインスタンスを初期化します。

        Args:
            first_name (str): キャラクターの名前。
            is_alive (bool, optional): 生存状態。デフォルトは True。
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        キャラクターを死亡状態に設定します。
        """
        self.is_alive = False

    def __str__(self):
        """
        インスタンスを文字列で表現します。

        Returns:
            str: インスタンスの文字列表現。
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        インスタンスを再現可能な文字列で表現します。

        Returns:
            str: インスタンスの再現可能な文字列表現。
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """
    Lannister 家を表現するクラス。

    Attributes:
        family_name (str): 家族名 "Lannister" を保持します。
        eyes (str): 目の色。初期値は "blue" です。
        hairs (str): 髪の色。初期値は "light" です。
    """

    def __init__(self, first_name, is_alive=True):
        """
        Lannister クラスのインスタンスを初期化します。

        Args:
            first_name (str): キャラクターの名前。
            is_alive (bool, optional): 生存状態。デフォルトは True。
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        キャラクターを死亡状態に設定します。
        """
        self.is_alive = False

    def __str__(self):
        """
        インスタンスを文字列で表現します。

        Returns:
            str: インスタンスの文字列表現。
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        インスタンスを再現可能な文字列で表現します。

        Returns:
            str: インスタンスの再現可能な文字列表現。
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        クラスメソッドを用いて Lannister のインスタンスを生成します。

        Args:
            first_name (str): キャラクターの名前。
            is_alive (bool, optional): 生存状態。デフォルトは True。

        Returns:
            Lannister: 生成された Lannister のインスタンス。
        """
        return cls(first_name, is_alive)


if __name__ == '__main__':
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, \
    Alive : {Jaine.is_alive}")
