#  Phannawich 934486183
import time
import os
from . import clear_screen

def main():
    clear_screen()
    while True:
        print("=== Use Item ===")
        print("1. Small HP Potion")
        print("2. Large HP Potion")
        print("3. Small EXP Potion")
        print("4. Large EXP Potion")
        print("0. Return to Main Menu")
        
        choice = input("Enter your choice (1-4 or 0 to exit): ").strip()
        if choice in ['1', '2', '3', '4']:
            try:
                with open(os.path.join(os.path.dirname(__file__), "use_item_transmission.txt"), "w") as file:
                    file.write(choice)
            except PermissionError:
                print("Permission denied: Unable to write to use_item_transmission.txt.")
                return

            # Wait for the response from use_item_backend.py
            start_time = time.time()
            while True:
                if time.time() - start_time > 10:
                    print("No response from backend. Please try again.")
                    break
                try:
                    with open(os.path.join(os.path.dirname(__file__), "use_item_transmission.txt"), "r") as file:
                        response = file.read().strip()
                        if response == 'yes':
                            print("Item used successfully!")
                            input("Press Enter to continue...")
                            break
                        elif response == 'no':
                            print("Failed to use item: Not enough in inventory.")
                            input("Press Enter to continue...")
                            break
                except FileNotFoundError:
                    pass
                except PermissionError:
                    print("Permission denied: Unable to read from use_item_transmission.txt.")
                    return

            clear_screen()
        elif choice == '0':
            return
        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
