"""information provided during Lecture 3
Guessing game with files and exceptions
"""

FILENAME = "secret.txt"


def main():
    secret = load_number(FILENAME)
    guess = get_valid_number()

    while guess != secret:
        print("Guess again!")
        guess = get_valid_number()
    print("You got it")

    """
    is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)"""


def get_valid_number() -> int:
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer")
    return guess  # no problem with potential undefined variable


def load_number(filename):
    """Load integer from file filename"""
    infile = open(filename, "r")
    try:
        number = int(infile.read())
    except ValueError:
        print(f"Inbalid contents in {filename}")
        number = 6
    except FileNotFoundError:
        print(f"This {filename} not found")
        number = 4
    else:
        infile.close()
    return number


main()
