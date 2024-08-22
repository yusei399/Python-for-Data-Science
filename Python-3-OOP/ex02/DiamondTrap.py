from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        self.eyes = color
    
    def set_hairs(self,  color):
        self.hairs = color

    def get_eyes(self):
        return self.eyes
        
    def get_hairs(self):
        return self.hairs


if __name__ == "__main__":
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)