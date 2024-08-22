from S1E9 import Character

class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

        def die(self):
            self.is_alive = False

#your code here
class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        self.is_alive = False
    # decorator
    @classmethod 
    def create_lannister(cls, first_name, is_alive):
        generate_instance = cls(first_name)
        generate_instance.is_alive = is_alive
        return generate_instance


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
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")