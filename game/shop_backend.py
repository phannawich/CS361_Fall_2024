# shop_backend.py
import json
import os
import time

def main():
    transmission_file = os.path.join(os.path.dirname(__file__), "shop_transmission.txt")
    character_file = os.path.join(os.path.dirname(__file__), "character.json")
    
    # Price Table and Item Mapping
    price_table = {
        '1': 5,   # Small HP Potion
        '2': 10,  # Large HP Potion
        '3': 10,  # Small EXP Potion
        '4': 15   # Large EXP Potion
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
                if choice in price_table:
                    # Load character data
                    with open(character_file, "r") as char_file:
                        character = json.load(char_file)
                    
                    price = price_table[choice]
                    if character["coin"] >= price:
                        # Deduct the coin and add item to inventory
                        character["coin"] -= price
                        item_name = item_table[choice]
                        character["inventory"].setdefault(item_name, 0)
                        character["inventory"][item_name] += 1
                        try:
                            with open(character_file, "w") as char_file:
                                json.dump(character, char_file, indent=4)
                            # Write success response
                            with open(transmission_file, "w") as file:
                                file.write("yes")
                        except PermissionError:
                            print("Permission denied: Unable to write to character.json or shop_transmission.txt.")
                    else:
                        # Write failure response
                        with open(transmission_file, "w") as file:
                            file.write("no")
        except FileNotFoundError:
            continue
        except PermissionError:
            print("Permission denied: Unable to read from shop_transmission.txt or character.json.")
            continue

if __name__ == "__main__":
    main()
