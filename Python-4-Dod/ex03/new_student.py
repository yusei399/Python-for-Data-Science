import sys
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    ランダムな15文字の小文字のIDを生成して返します。

    Returns:
        str: 生成されたID文字列。
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    学生を表すクラス。

    Attributes:
        name (str): 学生の名前。
        surname (str): 学生の苗字。
        active (bool): 学生のアクティブ状態（デフォルトはTrue）。
        login (str): 学生のログイン名。名前の先頭文字を大文字にし、苗字と連結して作成される。
        id (str): 学生のID。ランダムな15文字の小文字で生成される。
    """

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __init__(self, name: str, surname: str, active: bool = True, **kwargs):
        """
        学生オブジェクトを初期化します。

        Args:
            name (str): 学生の名前。
            surname (str): 学生の苗字。
            active (bool, optional): アクティブ状態（デフォルトはTrue）。

        Raises:
            TypeError: 想定外のキーワード引数が渡された場合に発生する。
        """
        if kwargs:
            sys.tracebacklimit = 0
            unexpected_key = next(iter(kwargs))
            raise TypeError(
                f"Student.__init__() got an unexpected keyword argument "
                f"'{unexpected_key}'"
            )
        self.name = name
        self.surname = surname
        self.active = active
        self.__post_init__()

    def __post_init__(self):
        """
        ログイン名とIDを初期化します。

        ログイン名は、名前の先頭文字を大文字にし苗字と連結して作成されます。
        IDは、ランダムな15文字の小文字で生成されます。
        """
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()
