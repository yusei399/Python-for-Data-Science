import sys

args = sys.argv

if len(args) == 1:
    exit()

if len(args) > 2:
    raise AssertionError("more than one argument is provided")

try:
    num = int(args[1])
except ValueError:
    raise AssertionError("argument is not an integer")

if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")

