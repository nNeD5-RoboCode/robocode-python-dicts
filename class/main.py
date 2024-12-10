import string
from datetime import datetime
from tabulate import tabulate


options = [
    "Menu",
    "Show",
    "Add",
    "Exit without save",
]
minercaft_review = {
    "Name": "MineCraft",
    "genre": "sandbox",
    "score": 8.0,
    "release year": 2010,
    "finish game date": datetime.now(),
}
games_reviews = [minercaft_review, minercaft_review, minercaft_review]

def print_menu():
    title = "Reviews Menu"
    print(f"\n\033[92m==== {title} ====\033[0m")
    for n, option in enumerate(options):
        print(f"  {n}. {option}")

def print_reviews():
    formated_reviews = []
    for review in games_reviews:
        d = review.copy()
        d["finish game date"] = d["finish game date"].strftime("%Y-%m-%d")
        formated_reviews.append(d)
    print(tabulate(formated_reviews, headers="keys", tablefmt="fancy_grid"))

def add_review():
    name = input("Enter game name: ").strip()
    if not name:
        print("Sorry, invalid game name (Empty)")
        return

    genre = input("Enter game genre: ").stip()

    relesease_year = input("Enter release year: ").strip()
    if release_year.isnumeric():
        relesease_year = int(relesease_year)
    else:
        relesease_year = None

    finish_game_date = input("Enter finish game date: ").strip()


def exit_menu():
    exit()

options_binds = [
    print_menu,
    print_reviews,
    exit_menu,
]


def main():
    print_menu()
    while True:
        user_choice = int(input("Choose option: "))
        options_binds[user_choice]()

main()
