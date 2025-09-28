"""

Write a complete Python program following the standard structure that uses a main and other functions.
Use a main menu following the standard menu pattern.

The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
Handle each of these (except quit) separately, and consider how you can reuse your functions.

In main(), before the menu loop, get a valid score using your function.
When the user quits, say some kind of "farewell"."""


def main():
    score = int(input("Score: "))
    score = get_valid_score(score)

    # when valid  and evaluate it
    determine_result(score)

    # print stars (same as score)
    show_stars(score)

def determine_result(score: int) -> int:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    return score


def get_valid_score(score: int) -> int:
    while score <= 0 or score > 100:
        print("This is an invalid score")
        print("Score must be between 0-100")
        score = int(input("Score: "))
    return score

def show_stars(score:int):
    print("*" * score)

main()
# print(f"Your score is, {score}")
