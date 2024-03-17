import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
    "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "
}

def encode_to_morse(text):
    encoded_message = ''
    for char in text:
        if char.upper() in NESTED_MORSE:
            encoded_message += NESTED_MORSE[char.upper()]
        else:
            raise AssertionError("the arguments are bad")
    return encoded_message.strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
    else:
        input_text = sys.argv[1]
        try:
            morse_code = encode_to_morse(input_text)
            print(morse_code, end='')
        except AssertionError as error:
            print(error)
