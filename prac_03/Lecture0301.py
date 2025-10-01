"""information provided during Lecture 3
Guessing game with files and exceptions
"""

FILENAME = "secret.txt"





def main():
    secret = load_number(FILENAME)
    guess = int(input("? "))
    while guess != secret:
        print("Guess again!")
        guess = int(input("? "))
    print("You got it")

def load_number(filename):
    """Load integer from file filename"""
    infile = open(filename, "r")
    number = int(infile.read())
    infile.close()
    return number

main()

