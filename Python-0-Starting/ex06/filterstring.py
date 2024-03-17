import sys

def filterstring(string: str, integer: int) -> list:
    string = string.split()
    return [char for char in string if len(char) > integer]

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        string = sys.argv[1]
        integer = int(sys.argv[2])
        print(filterstring(string, integer))
    except (AssertionError, ValueError) as e:
        print(e)
