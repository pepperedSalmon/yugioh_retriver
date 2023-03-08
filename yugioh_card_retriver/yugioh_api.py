import requests
import json
from yugioh_objects import MonsterCard
from yugioh_objects import SpellTrapCard
from yugioh_objects import YugiohCard


def get_online_data(cards,jsonName):
    """This function gets yugioh cards info from YGOPro 
        then we save the information into a local Json file"""
     
    # Make an API call and store the response.
    url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?'+cards
    r = requests.get(url)
    print(f"Status code: {r.status_code}")

    # Store API response in a variable.
    response_dict = r.json()
    # Save API response as json file locally.
    filename = f'{jsonName}.json'
    with open(filename, 'w') as f:
            json.dump(response_dict, f)

class YugiohSet:
    "Reads information from Json file we got from YGO PRO API to create yugioh card objects"
    def __init__(self,file_name):
        self.file_name=file_name
        self.cards=[]
        self.build()
        self.len=len(self.cards)
    def build(self):
        # 
        try: 
            with open(self.file_name) as f:
                response_dict=json.load(f)
        except FileNotFoundError:
            print(f"Sorry, the file {filename} does not exist.")
        else:
            cards_dicts = response_dict['data']
            
            for card in cards_dicts:
                if "Monster" in card['type']:
                    self.cards.append(MonsterCard(name=card['name'],
                                            frame=card['type'],
                                            rarity=[set["set_name"] for set in card["card_sets"]],
                                            card_set= [set["set_rarity"] for set in card["card_sets"]],
                                            text=card["desc"],
                                            atribute=card["attribute"],
                                            monster_type=card["race"],
                                            level=card["level"],
                                            _atk=card["atk"],
                                            _def=card["def"],
                                            s_frame="Monster Card",
                                            img_url=card["card_images"][0]["image_url"]))

                elif "Spell" in card['type']:
                    self.cards.append(SpellTrapCard(name=card['name'],
                                            frame=card['type'],
                                            rarity=[set["set_name"] for set in card["card_sets"]],
                                            card_set= [set["set_rarity"] for set in card["card_sets"]],
                                            text=card["desc"],
                                            card_icon=card["race"],
                                            s_frame="Spell Card",
                                            img_url=card["card_images"][0]["image_url"]))

                elif "Trap" in card['type']:
                    self.cards.append(SpellTrapCard(name=card['name'],
                                            frame=card['type'],
                                            rarity=[set["set_name"] for set in card["card_sets"]],
                                            card_set= [set["set_rarity"] for set in card["card_sets"]],
                                            text=card["desc"],
                                            card_icon=card["race"],
                                            s_frame="Trap Card",
                                            img_url=card["card_images"][0]["image_url"]))
                elif "Skill" in card['type']:
                   self.cards.append(YugiohCard(name=card['name'],
                                            frame=card['type'],
                                            rarity=[set["set_name"] for set in card["card_sets"]],
                                            card_set= [set["set_rarity"] for set in card["card_sets"]],
                                            text=card["desc"],
                                            s_frame="Skill Card",
                                            img_url=card["card_images"][0]["image_url"]))
                else:
                    print("??? I dont know what this is!")





