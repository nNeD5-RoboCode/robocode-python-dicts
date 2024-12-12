import menu

def main():
    menu.print_menu()
    while True:
        user_choice = int(input("Choose option: "))
        menu.options_binds[user_choice]()


if __name__ == "__main__":
    main()
