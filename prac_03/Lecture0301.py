"""information provided during Lecture 3
"""

def main():
    secret = 6
    guess = int(input("? "))
    while guess != secret:
        print("Guess again!")
        guess = int(input("? "))
    print("You got it")

main()

