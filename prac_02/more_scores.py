"""
CP1404/CP5632 - Practical
Ask the user for a number of scores
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt as below:
"""

import random


# The intention is that the score must be between 0 and 100 inclusive;
# 90 or more is excellent;
# 50 or more is a pass;


def main():
    user_input = input("Enter a score (or press enter for a random score): ")

    if user_input == "":
        # no input received from user
        score = random.randint(0, 100)
        print(f"no score was given, here is your random score: {score}")
    else:
        # input received from user and evaluated
        score = float(user_input)

    evaluate_score(score)


def evaluate_score(score: float):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()