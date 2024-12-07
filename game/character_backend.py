import json
import os
import time

def main():
    character_file = os.path.join(os.path.dirname(__file__), "character.json")
    
    while True:
        time.sleep(1)
        try:
            with open(character_file, "r") as char_file:
                character = json.load(char_file)
            
            if character["exp"] >= character["maxexp"]:
                character["exp"] = 0
                character["hp"] = character["maxhp"]
                character["coin"] += 10
                
                with open(character_file, "w") as char_file:
                    json.dump(character, char_file, indent=4)
        except FileNotFoundError:
            print("Error: character.json not found.")
            continue
        except json.JSONDecodeError:
            print("Error: character.json is not a valid JSON file.")
            continue
        except PermissionError:
            print("Permission denied: Unable to read or write character.json.")
            continue

if __name__ == "__main__":
    main()