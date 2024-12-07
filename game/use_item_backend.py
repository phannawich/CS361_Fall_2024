import json
import os
import time

def main():
    transmission_file = os.path.join(os.path.dirname(__file__), "use_item_transmission.txt")
    character_file = os.path.join(os.path.dirname(__file__), "character.json")
    
    # Effect Table
    effect_table = {
        '1': {"type": "hp", "amount": 5},   # Small HP Potion
        '2': {"type": "hp", "amount": 10},  # Large HP Potion
        '3': {"type": "exp", "amount": 50}, # Small EXP Potion
        '4': {"type": "exp", "amount": 100} # Large EXP Potion
    }
    item_table = {
        '1': "Small HP Potion",
        '2': "Large HP Potion",
        '3': "Small EXP Potion",
        '4': "Large EXP Potion"
    }
    
    while True:
        time.sleep(1)  # Check every 1 second
        try:
            with open(transmission_file, "r") as file:
                choice = file.read().strip()
                if choice in effect_table:
                    # Load character data
                    with open(character_file, "r") as char_file:
                        character = json.load(char_file)
                    
                    item_name = item_table[choice]
                    if character["inventory"].get(item_name, 0) > 0:
                        # Apply the effect
                        effect = effect_table[choice]
                        if effect["type"] == "hp":
                            character["hp"] = min(character["hp"] + effect["amount"], character["maxhp"])
                        elif effect["type"] == "exp":
                            character["exp"] = min(character["exp"] + effect["amount"], character["maxexp"])
                        
                        # Decrease the item count
                        character["inventory"][item_name] -= 1
                        
                        try:
                            with open(character_file, "w") as char_file:
                                json.dump(character, char_file, indent=4)
                            # Write success response
                            with open(transmission_file, "w") as file:
                                file.write("yes")
                        except PermissionError:
                            print("Permission denied: Unable to write to character.json or use_item_transmission.txt.")
                    else:
                        # Write failure response
                        with open(transmission_file, "w") as file:
                            file.write("no")
        except FileNotFoundError:
            continue
        except PermissionError:
            print("Permission denied: Unable to read from use_item_transmission.txt or character.json.")
            continue

if __name__ == "__main__":
    main()
