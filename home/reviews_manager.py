from datetime import datetime

from tabulate import tabulate


minercaft_review = {
    "name": "MineCraft",
    "genre": "sandbox",
    "score": 8.0,
    "release year": 2010,
    "finish game date": datetime.now().date(),
}
games_reviews = [minercaft_review, minercaft_review, minercaft_review]



def print_reviews():
    print(tabulate(games_reviews, headers="keys", tablefmt="fancy_grid"))


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

