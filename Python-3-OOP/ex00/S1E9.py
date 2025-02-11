from abc import ABC, abstractmethod


class Character(ABC):
    """
    抽象基底クラス: Character

    Attributes:
        first_name (str): キャラクターの名前
        is_alive (bool): キャラクターが生存しているかどうかのフラグ
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Character クラスの初期化メソッド

        Args:
            first_name (str): キャラクターの名前
            is_alive (bool, optional): キャラクターが生存しているかどうか. デフォルトは True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """
        キャラクターを死亡状態にするメソッド

        このメソッドはサブクラスで上書きされることを想定しています。
        """
        pass


class Stark(Character):
    """
    具象クラス: Stark

    House Stark のキャラクターを表現します。
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Stark クラスの初期化メソッド

        Args:
            first_name (str): Stark キャラクターの名前
            is_alive (bool, optional): キャラクターが生存しているかどうか. デフォルトは True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """
        Stark キャラクターを死亡状態にするメソッド

        is_alive 属性を False に設定します。
        """
        self.is_alive = False


if __name__ == '__main__':
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
