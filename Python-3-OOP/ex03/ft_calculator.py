
class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object):
        """Adds a scalar to each element of the vector and prints the result."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object):
        """Multiplies each element of the vector by a scalar and prints the result."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object):
        """Subtracts a scalar from each element of the vector and prints the result."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object):
        """Divides each element of the vector by a scalar and prints the result."""
        self.vector = [x / object for x in self.vector]
        print(self.vector)


