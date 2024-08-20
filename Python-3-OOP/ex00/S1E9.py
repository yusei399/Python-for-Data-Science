from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self, firstname:str, is_alive=True):
        self.firstname = firstname
        self.is_alive = is_alive

    def die(self) -> None:
        pass



class Stark(Character):
    def __init__(self, firstname: str, is_alive=True):
        self.firstname = firstname
        self.is_alive = is_alive


    def die(self):
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