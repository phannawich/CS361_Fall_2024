import json
import random
import time
from game import clear_screen
import os

def load_character():
    """Loads character data from character.json."""
    try:
        with open(os.path.join(os.path.dirname(__file__), 'character.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: character.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: character.json is not a valid JSON file.")
        return None

def load_dictionary():
    """Loads words from dictionary.json."""
    try:
        with open(os.path.join(os.path.dirname(__file__), 'dictionary.json'), 'r') as f:
            data = json.load(f)
            return data.get("words", [])
    except FileNotFoundError:
        print("Error: dictionary.json not found.")
        return []
    except json.JSONDecodeError:
        print("Error: dictionary.json is not a valid JSON file.")
        return []

def display_instructions():
    """Displays typing game instructions."""
    print("=== Go typing Instructions ===")
    print("You will have to type as fast as you can to gain Experince point (EXP)")
    print("Accumulating EXP will help you level up your character")
    print("Be careful! Incorrect typings might affect your health point (HP)")
    print("=================================")
    
    while True:
        choice = input("Do you ready to play the game (1:Yes, 0:No): ").strip()
        if choice == '1':
            return True  # Proceed to start the game
        elif choice == '0':
            return False  # Exit to main menu
        else:
            print("Invalid input. Please enter '1' to start or '0' to return to the main menu.")

def display_character_status(character):
    """Displays the character's HP and EXP status."""
    print("=== Character Status ===")
    print(f"HP: {character['hp']}/{character['maxhp']}")
    print(f"EXP: {character['exp']}/{character['maxexp']}")
    print("========================")
    print()

def save_character(character):
    """Saves the updated character data back to character.json."""
    try:
        with open(os.path.join(os.path.dirname(__file__), 'character.json'), 'w') as f:
            json.dump(character, f, indent=4)
    except Exception as e:
        print(f"Error saving character data: {e}")

def calculate_accuracy(expected, actual):
    """Calculates the accuracy percentage between expected and actual input."""
    expected_chars = list(expected)
    actual_chars = list(actual)
    correct = sum(1 for ew, aw in zip(expected_chars, actual_chars) if ew == aw)
    total = len(expected_chars)
    return (correct / total) * 100 if total > 0 else 0

def main():
    clear_screen()
    
    character = load_character()
    if not character:
        input("Press Enter to return to the main menu...")
        return
    
    display_character_status(character)
    proceed = display_instructions()
    if not proceed:
        return


    words = load_dictionary()
    if not words:
        input("Press Enter to return to the main menu...")
        return

    clear_screen()
    print("Starting the Typing Game...")
    time.sleep(2)
    clear_screen()

    display_character_status(character)

    score = 0
    mistakes = 0
    total_words = 10

    for i in range(1, total_words + 1):
        word = random.choice(words)
        print(f"Word {i}/{total_words}:")
        print(f"{word}")
        start_time = time.time()
        user_input = input("Your input: ").strip()
        end_time = time.time()

        time_taken = end_time - start_time
        accuracy = calculate_accuracy(word, user_input)

        if user_input == word:
            exp_gained = 10
            print(f"Correct! (+{exp_gained} EXP) Time taken: {time_taken:.2f} seconds\n")
            score += exp_gained
            character['exp'] += exp_gained
        else:
            hp_lost = 5
            print(f"Incorrect! (-{hp_lost} HP)")
            print(f"Expected: '{word}'")
            print(f"Your Input: '{user_input}'")
            print(f"Accuracy: {accuracy:.2f}%\n")
            mistakes += 1
            character['hp'] -= hp_lost

        display_character_status(character)

        if character['hp'] <= 0:
            print("Your HP has dropped to 0! Game Over.")
            break

        time.sleep(1)
        clear_screen()

    if character['hp'] > 0:
        print("Typing session completed.")
    print(f"Score: {score}")
    print(f"Mistakes: {mistakes}")

    if character['exp'] >= character['maxexp']:
        character['exp'] -= character['maxexp']
        character['maxexp'] += 50
        print("Congratulations! You've leveled up!")
        print(f"New EXP requirement for next level: {character['maxexp']}")
    else:
        print(f"Current EXP: {character['exp']}/{character['maxexp']}")

    save_character(character)

    input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    main()
