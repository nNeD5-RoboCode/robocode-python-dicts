from datetime import date

from tabulate import tabulate
from typing import TypedDict
import json
import os


GameReview = TypedDict(
    "GameReview",
    {
        "name": str,
        "genre": str | None,
        "score": float | None,
        "release year": int | None,
        "finish game date": date | str | None,
    },
)

minercaft_review: GameReview = {
    "name": "MineCraft",
    "genre": "sandbox",
    "score": 8.0,
    "release year": 2010,
    "finish game date": date.today(),
}
games_reviews: list[GameReview] = [minercaft_review, minercaft_review, minercaft_review]


def print_reviews():
    print(
        tabulate(games_reviews, headers="keys", tablefmt="fancy_grid", showindex=True)
    )


def delete_review():
    print_reviews()
    select = input("Enter game number to delete: ").strip()
    if select.isnumeric() and int(select) < len(games_reviews):
        review = games_reviews.pop(int(select))
        print(tabulate([review], headers="keys", tablefmt="fancy_grid"))
    else:
        print(f"Sorry, {select} invalid index (not numeric or out of bonds)")
    print_reviews()


def add_review():
    # add name
    name = input("Enter game name: ").strip()
    if not name:
        print("Sorry, invalid game name (Empty)")
        return

    review: GameReview = {
        "name": name,
        "genre": None,
        "score": None,
        "release year": None,
        "finish game date": None,
    }

    # add score
    score = input(f"Enter score (max 10) for {name}: ").strip()
    if score.isnumeric() and float(score) <= 10:
        score = float(score)
    else:
        print(f"Sorry, `{score}` is invalid score (not numeric or >10)")
        score = None
    review["score"] = score

    # add genre
    genre = input("Enter game genre: ").strip()
    review["genre"] = genre

    # add release year
    release_year = input("Enter release year: ").strip()
    if release_year.isnumeric():
        release_year = int(release_year)
    else:
        print(f"Sorry, `{release_year}` is invalid release year (not integer)")
        release_year = None
    review["release year"] = release_year

    finish_game_date = input("Enter finish game date(%Y %m %d): ").strip().split()

    finish_year = None
    finish_month = None
    finish_day = None
    if len(finish_game_date) >= 1 and finish_game_date[0].isnumeric():
        finish_year = int(finish_game_date[0])
    if (
        len(finish_game_date) >= 2
        and finish_game_date[1].isnumeric()
        and int(finish_game_date[1]) <= 12
    ):
        finish_month = int(finish_game_date[1])
    if (
        len(finish_game_date) >= 3
        and finish_game_date[2].isnumeric()
        and int(finish_game_date[1]) <= 31
    ):
        finish_day = int(finish_game_date[2])

    if finish_year and finish_month and finish_day:
        finish_game_date = date(year=finish_year, month=finish_month, day=finish_day)
        review["finish game date"] = finish_game_date
    else:
        print(f"Sorry, `{finish_game_date}` is invalid date")
    games_reviews.append(review)
    print_reviews()


def date_encoded(obj): # pyright: ignore[reportMissingParameterType,reportUnknownParameterType]
    if isinstance(obj, date):
        return obj.isoformat()

def date_decode(empDict: GameReview):
   if "finish game date" in empDict:
      empDict["finish game date"] = date.fromisoformat(str(empDict["finish game date"]))
      return empDict


def save_reviews():
    print_reviews()
    with open("games_reviews.json", "w") as f:
        json.dump(games_reviews, f, default=date_encoded) # pyright: ignore[reportUnknownArgumentType]


def load_reviews():
    if not os.path.isfile("games_reviews.json"):
        print("Sorry, games_reviews.json does not exit")
        return
    with open("games_reviews.json", "r") as f:
        global games_reviews
        games_reviews = json.load(f, object_hook=date_decode) # pyright: ignore[reportArgumentType]
    print_reviews()
