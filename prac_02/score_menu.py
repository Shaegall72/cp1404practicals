# display menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     else if choice == <second option>
#         <do second task>
#     ...
#     else if choice == <n-th option>
#         <do n-th task>
#     else
#         display invalid input error message
#     display menu
#     get choice
# <do final thing, if needed>

# G get valid (non-empty) name
# P print greeting
# S print secret name (random variation)
"""This program will
get a valid score between 0-100

Print and determine the result
show stars the qty of the result
quit"""


names = ()

def main():
    name = "Shae Machin"
    print("Menu: (G)et name, (P)rint name, (S)tars (Q)uit.")
    menu_choice = input("> ").upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            name = get_valid_name()
        elif menu_choice == "P":
            print_greeting(name)
        elif menu_choice == "S":
           pass
        else:
            print("Invalid selection")
        print("Menu: ")
        menu_choice = input("> ").upper()

    print("Goodbye")


def print_greeting(name: str):
    length = len(name)
    print_line(length)
    print(name)
    print_line(length)


def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("This is an invalid name")
        name = input("Name: ")
    return name

def print_line(length):
    print('-' * length)

def print_secret_name(name):



    main()
