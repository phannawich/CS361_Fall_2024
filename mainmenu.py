import sys
from game import clear_screen
from game import character, go_typing, use_item, shop

def display_welcome():
    """Displays the welcome message."""
    print("=======================================")
    print("    Welcome to the Speed Typing RPG!    ")
    print("=======================================")
    print()
    print("You will speed typing and gain exp and progress in this game")
    print()

def display_menu():
    """Displays the main menu options."""
    print("Main Menu:")
    print("1. Character Page")
    print("2. Go Typing")
    print("3. Use Item")
    print("4. Shop")
    print("0. Close the Program")
    print()

def main():
    """Main function to run the main menu loop."""
    while True:
        clear_screen()
        display_welcome()
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            character.main()
        elif choice == '2':
            go_typing.main()
        elif choice == '3':
            use_item.main()
        elif choice == '4':
            shop.main()
        elif choice == '0' or choice == 'exit':
            print("Thank you for playing! Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
