from typing import Callable

import reviews_manager

options = [
    "Exit without save",
    "Show",
    "Add",
    "Delete",
    "Save",
    "Save & exit",
]


def print_menu():
    title = "Reviews Menu"
    print(f"\n\033[92m==== {title} ====\033[0m")
    for n, option in enumerate(options):
        print(f"  {n}. {option}")


def exit_menu():
    exit()


def save_and_exit():
    reviews_manager.save_reviews()
    exit_menu()


options_binds: list[Callable[[], None]] = [
    exit_menu,
    reviews_manager.print_reviews,
    reviews_manager.add_review,
    reviews_manager.delete_review,
    reviews_manager.save_reviews,
    save_and_exit,
]
