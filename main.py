import menu
import reviews_manager


def main():
    reviews_manager.load_reviews()
    reviews_manager.print_reviews()
    menu.print_menu()
    while True:
        user_choice = int(input("Choose option: "))
        menu.options_binds[user_choice]()
        menu.print_menu()


if __name__ == "__main__":
    main()
