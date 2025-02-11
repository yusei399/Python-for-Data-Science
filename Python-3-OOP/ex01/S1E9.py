from abc import ABC, abstractmethod


class Character(ABC):
    """
    キャラクターを表現する抽象基底クラス。

    Attributes:
        first_name (str): キャラクターの名前。
        is_alive (bool): キャラクターが生存しているかどうか。
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """
        キャラクターの初期化を行います。

        Args:
            first_name (str): キャラクターの名前。
            is_alive (bool, optional): キャラクターが生存しているかどうか。
                デフォルトは True。
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """
        キャラクターを死亡状態にします。

        このメソッドはサブクラスで具体的な実装を行うことを想定しています。
        """
        pass


class Stark(Character):
    """
    Stark ファミリーのキャラクターを表す具象クラス。
    """

    def __init__(self, first_name: str, is_alive=True):
        """
        Stark キャラクターの初期化を行います。

        Args:
            first_name (str): キャラクターの名前。
            is_alive (bool, optional): キャラクターが生存しているかどうか。
                デフォルトは True。
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """
        Stark キャラクターを死亡状態に設定します。
        """
        self.is_alive = False
