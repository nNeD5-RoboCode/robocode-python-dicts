from datetime import datetime

from tabulate import tabulate


options = [
    "Menu",
    "Show",
    "Add",
    "Exit without save",
]
minercaft_review = {
    "name": "MineCraft",
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
        d["finish game date"] = d["finish game date"].strftime("%Y-%m-%d")  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
        formated_reviews.append(d)  # pyright: ignore[reportUnknownMemberType]
    print(tabulate(formated_reviews, headers="keys", tablefmt="fancy_grid"))  # pyright: ignore[reportUnknownArgumentType]


def add_review():
    name = input("Enter game name: ").strip()
    if not name:
        print("Sorry, invalid game name (Empty)")
        return

    score = input(f"Enter score for {name}: ").strip()
    if score.isnumeric():
        score = float(score)
    else:
        score = ""

    genre = input("Enter game genre: ").strip()

    release_year = input("Enter release year: ").strip()
    if release_year.isnumeric():
        release_year = int(release_year)
    else:
        release_year = ""

    finish_game_date = input("Enter finish game date: ").strip()
    games_reviews.append(
        {
            "name": name,
            "genre": genre,
            "score": score,
            "release year": release_year,
            "finish game date": finish_game_date,
        }
    )


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
        user_choice = int(input("Choose option: "))
        options_binds[user_choice]()


if __name__ == "__main__":
    main()
