"""Print asterisks as long as word"""


def main():
    print("Enter a password longer than 6 letters")
    password_length = get_password()

    # ensure word is longer than 6 letters
    while password_length <= 6:
        print(f"Not long enough, try again")
        password_length = get_password()

    # correct length entered
    else:
        password_stars(password_length)


def password_stars(password_length: int):
    total_stars = "*" * password_length
    print(total_stars)


def get_password() -> int:
    password = input("Password: ")
    password_length = len(password)
    return password_length


main()
