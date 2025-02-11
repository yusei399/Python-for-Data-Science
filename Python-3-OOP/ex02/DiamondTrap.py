from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """
    King クラス
    Baratheon と Lannister の多重継承により、初期状態は Baratheon の属性が継承される。
    プロパティを使って、目と髪の色を動的に変更できます。
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    @property
    def eyes(self):
        return self.__dict__['eyes']

    @eyes.setter
    def eyes(self, color):
        self.__dict__['eyes'] = color

    @property
    def hairs(self):
        return self.__dict__['hairs']

    @hairs.setter
    def hairs(self, color):
        self.__dict__['hairs'] = color

    def set_eyes(self, color):
        """プロパティを利用して目の色を変更する"""
        self.eyes = color

    def set_hairs(self, color):
        """プロパティを利用して髪の色を変更する"""
        self.hairs = color

    def get_eyes(self):
        """プロパティを利用して目の色を取得する"""
        return self.eyes

    def get_hairs(self):
        """プロパティを利用して髪の色を取得する"""
        return self.hairs



if __name__ == "__main__":
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)