import json
import random
import time
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_dictionary():
    """Loads words from dictionary.json."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "dictionary.json")
        with open(file_path, "r") as f:
            data = json.load(f)
            return data.get("words", [])
    except FileNotFoundError:
        print("Error: dictionary.json not found.")
        return []
    except json.JSONDecodeError:
        print("Error: dictionary.json is not a valid JSON file.")
        return []

def load_character():
    """Loads character data from character.json."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "character.json")
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: character.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: character.json is not a valid JSON file.")
        return None

def save_character(character):
    """Saves character data to character.json."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "character.json")
        with open(file_path, "w") as f:
            json.dump(character, f, indent=4)
    except Exception as e:
        print(f"Error saving character data: {e}")

def write_to_file(file_path, content):
    """Writes content to a file."""
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

def read_from_file(file_path):
    """Reads content from a file."""
    try:
        with open(file_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

def display_instructions():
    """Displays typing game instructions."""
    print("=== Go Typing Instructions ===")
    print("You will have to type as fast as you can to gain Experience Points (EXP).")
    print("Accumulating EXP will help you level up your character.")
    print("Be careful! Incorrect typings might affect your score and EXP gain.")
    print("=================================")

    while True:
        choice = input("Are you ready to play the game? (1: Yes, 0: No): ").strip()
        if choice == "1":
            return True
        elif choice == "0" or choice.lower() == "exit":
            return False
        else:
            print("Invalid input. Please enter '1' to start or '0' to return to the main menu.")

def display_character_status(character):
    """Displays the character's current HP and EXP."""
    print("=== Character Status ===")
    print(f"HP: {character['hp']}/{character['maxhp']}")
    print(f"EXP: {character['exp']}/{character['maxexp']}")
    print("========================")

def main():
    clear_screen()

    character = load_character()
    if not character:
        input("Press Enter to exit...")
        return

    words = load_dictionary()
    if not words:
        input("Press Enter to exit...")
        return

    display_character_status(character)

    if not display_instructions():
        return

    clear_screen()

    # Generate a prompt with 10-15 random words
    prompt_words = " ".join(random.sample(words, random.randint(10, 15)))
    write_to_file("prompt.txt", prompt_words)

    print("Type the following text:")
    print(prompt_words)

    start_time = time.time()
    user_input = input("Your input: ").strip()
    end_time = time.time()

    write_to_file("user_input.txt", user_input)

    time.sleep(1)  # Allow microserviceA to process
    result = read_from_file("compared_result.txt")

    if not result:
        print("Error: No response from microserviceA. Returning to main menu.")
        return

    try:
        correct, total = map(int, result.split("/"))
        accuracy = (correct / total) * 100 if total > 0 else 0
        time_taken = end_time - start_time

        exp_gained = correct * 10
        hp_lost = (total - correct) * 5

        character['exp'] += exp_gained
        character['hp'] -= hp_lost

        print(f"Result: {correct}/{total} correct words")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Time Taken: {time_taken:.2f} seconds")
        print(f"EXP Gained: {exp_gained}")
        print(f"HP Lost: {hp_lost}")

        if character['hp'] <= 0:
            print("Your HP has dropped to 0. Game Over!")
            character['hp'] = 0
        else:
            if character['exp'] >= character['maxexp']:
                character['exp'] -= character['maxexp']
                character['maxexp'] += 50
                print("Congratulations! You've leveled up!")
                print(f"New EXP requirement for next level: {character['maxexp']}")

        save_character(character)

    except ValueError:
        print("Error: Invalid response format from microserviceA.")

    # Clear all files
    write_to_file("prompt.txt", "")
    write_to_file("user_input.txt", "")
    write_to_file("compared_result.txt", "")

    input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    main()
