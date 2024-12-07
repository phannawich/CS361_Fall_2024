import json
import time
import os

from . import clear_screen

def load_character():
    """Loads character data from character.json."""
    character_file = os.path.join(os.path.dirname(__file__), "character.json")
    try:
        with open(character_file, "r") as char_file:
            return json.load(char_file)
    except FileNotFoundError:
        print("Error: character.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: character.json is not a valid JSON file.")
        return None

def display_character_status(character):
    """Displays the character's current status."""
    clear_screen()
    print("=== Character Status ===")
    print(f"HP: {character['hp']}/{character['maxhp']}")
    print(f"EXP: {character['exp']}/{character['maxexp']}")
    print(f"Coins: {character['coin']}")
    print("Inventory:")
    for item, amount in character["inventory"].items():
        print(f"  - {item}: {amount}")
    print("========================")
    print("0. Return to Main Menu")

def main():
    while True:
        character = load_character()
        if character:
            display_character_status(character)
            choice = input("Enter your choice: ").strip()
            if choice == '0':
                break
        else:
            print("Unable to load character information.")
            break
        
        time.sleep(5)

if __name__ == "__main__":
    main()