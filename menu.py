from typing import Callable
from . import reviews_manager

options = [
    "Menu",
    "Show",
    "Add",
    "Exit without save",
]

def print_menu():
    title = "Reviews Menu"
    print(f"\n\033[92m==== {title} ====\033[0m")
    for n, option in enumerate(options):
        print(f"  {n}. {option}")

def exit_menu():
    exit()


options_binds: list[Callable[[], None]] = [
     print_menu,
     reviews_manager.print_reviews,
     reviews_manager.add_review,
     exit_menu,
]


