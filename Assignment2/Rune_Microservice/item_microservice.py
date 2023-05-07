# Caleb Verstraete
# 5/4/23
# CS361: Microservice to which well receive requests for Runescape items in the txt file. Microservice
import time
import json


def main():
    item_dict = {"silver feather": {"Requirement": "Started Eagles' Peak quest",
                                    "Name": "Silver Feather",
                                    "Item number": "3653",
                                    "Quest": "Yes",
                                    "Found": "Eagles' Peak Caves",
                                    "Uses": "Used during the Eagles' Peak quest to open the door to the area with the eagles.",
                                    "Notes": "Can be reclaimed by from the Kebbit's lair in Eagles' Peak Cave.",
                                    "Weight": "0 kg",
                                    "Examine Information": "An intricate feather crafted from a silver-coloured metal of some sort."},
                 "hag's poison": {"Name": "Hag's  poison",
                                  "Requirement": "Must have started The Feud quest to use.",
                                  "Item number": "1867",
                                  "Quest": "Yes",
                                  "Found": "Given to you by Ali the Hag, at her house on the hill west of Pollnivneach, in exchange for a Snake basket (Full) and Ugthanki dung.",
                                  "Uses": "Used for The Feud quest.",
                                  "Notes": "Used on Traitorous Ali's Beer, at the pub in Pollnivneach, to kill him. If lost, it can be retrieved by talking to Ali the Hag again.",
                                  "Weight": "0 kg",
                                  "Examine Information": "A red viscous liquid in a vial."
                                  },
                 "jester hat": {"Name": "Jester hat",
                                "Requirement": "No requirements.",
                                "Item number": "2497",
                                "Quest": "No",
                                "Found": "Reward for completing the 2005 Christmas Event.",
                                "Uses": "Worn for decoration.",
                                "Notes": "Has been discontinued and can no longer be obtained.",
                                "Weight": "Unknown",
                                "Examine Information": "A woolly jester hat.",
                                "Combat Effects": {"Weapon Stats": {"Damage": "Unknown", "Accuracy": "Unknown"},
                                                   "Combat Bonuses": {"Strength": "Unknown", "Magic": "Unknown", "Ranged": "Unknown"},
                                                   "Attributes": {"Armour": "Unknown", "Life Bonus": "Unknown", "Prayer Bonus": "Unknown"},
                                                   "Styles": {"Class": "N/A", "Attack Style": "N/A", "Attack Speed": "N/A"}}},
                 "bronze 2h sword": {"Name": "Bronze 2h sword",
                                "Requirement": "1 Smithing to make (Exp: 60).",
                                "Item number": "165",
                                "Quest": "No",
                                "Found": "Player made (See Notes); Bought from Anton in the Warriors' Guild, from Gaius in Taverley, and from Gulluck in Tree Gnome Stronghold.",
                                "Uses": "Item used for melee attacks.",
                                "Notes": "Made by using 4 Bronze bars on an anvil. Can be used for looting Dung Kalphites.",
                                "Weight": "3 kg",
                                "Examine Information": "A two handed sword.",
                                "Dropped By": "White wolf (level 5)",
                                "Combat Effects": {"Weapon Stats": {"Damage": "111", "Accuracy": "150"},
                                                   "Combat Bonuses": {"Strength": "0.0", "Magic": "0.0", "Ranged": "0.0"},
                                                   "Attributes": {"Armour": "0", "Life Bonus": "0", "Prayer Bonus": "0"},
                                                   "Styles": {"Class": "Melee", "Attack Style": "Slashing", "Attack Speed": "Average"}}},
                 "bronze med helm": {"Name": "Bronze med helm",
                                "Requirement": "1 Defence to wear; 1 Smithing to make (Exp: 30).",
                                "Item number": "180",
                                "Quest": "No",
                                "Found": "Player made (See Notes); Monster drop; Bought from Anton in the Warriors' Guild, Gnome Shopkeeper in Burthorpe, Horvik in Varrock and Peska in the Barbarian Village; Respawns inside Draynor Village and Manor.",
                                "Uses": "Worn for protection.",
                                "Notes": "Made by using an anvil or forge with at least 2 bars in your inventory or metal bank. Note that you will need to have a hammer (inventory or toolbelt) or a hammertron in order to create this item. Creation of this item requires 200 progress to complete.",
                                "Weight": "1.81 kg",
                                "Examine Information": "A medium sized helmet.",
                                "Combat Effects": {"Weapon Stats": {"Damage": "0", "Accuracy": "0"},
                                                   "Combat Bonuses": {"Strength": "0.0", "Magic": "0.0", "Ranged": "0.0"},
                                                   "Attributes": {"Armour": "30", "Life Bonus": "0", "Prayer Bonus": "0"},
                                                   "Styles": {"Class": "Melee", "Attack Style": "N/A", "Attack Speed": "N/A"}}}}
    while True:
        time.sleep(2)
        with open('item_service.txt', 'r+', encoding='utf-8') as f:
            image_text = f.read().lower()
            print('item requested is: ' + image_text)
            if image_text != '' and image_text != 'item not here':
                if image_text in item_dict.keys():
                    f.truncate(0)
                    f.seek(0)
                    f.write(json.dumps(item_dict[image_text]))
                else:
                    f.truncate(0)
                    f.seek(0)
                    f.write('item not here')


if __name__ == '__main__':
    main()
