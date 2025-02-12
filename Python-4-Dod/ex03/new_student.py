import sys
import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __init__(self, name: str, surname: str, active: bool = True, **kwargs):
        # If any extra keyword arguments are provided (e.g., 'id' or 'login'),
        # set tracebacklimit to 0 so that only the error message is printed,
        # then raise the appropriate TypeError.
        if kwargs:
            sys.tracebacklimit = 0
            unexpected_key = next(iter(kwargs))
            raise TypeError(f"Student.__init__() got an unexpected keyword argument '{unexpected_key}'")
        self.name = name
        self.surname = surname
        self.active = active
        self.__post_init__()

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()


