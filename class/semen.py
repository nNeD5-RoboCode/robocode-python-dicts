from datetime import datetime
from tabulate import tabulate


minecraft = {
    "name": "MineCraft",
    "genre": "sandbox",
    "score": 8.0,
    "release year": 2010,
    "finish game date": datetime.now().date(),
}

games_reviews = [minecraft, minecraft, minecraft]

options = [
    "Menu",
    "Show",
    "Add",
    "Exit without save",
]


def print_menu():
    print("=== Reviews Menu ===")
    for n, option in enumerate(options):
        print(f"  {n}. {option}")


def print_reviews():
    print(tabulate(games_reviews, headers="keys", tablefmt="fancy_grid"))


def add_review(): ...


def exit_menu():
    exit()


options_binds = [
    print_menu,
    print_reviews,
    add_review,
    exit_menu,
]


def main():
    print_menu()
    while True:
        user_input = input("Choose option: ")
        options_number = int(user_input)
        options_binds[options_number]()


main()
