from yugioh_api import get_online_data
from yugioh_api import YugiohSet
import pandas as pd
import json 
import time

SpeedDuelProducts=['Speed Duel Starter Decks: Destiny Masters',
'Speed Duel Starter Decks: Duelists of Tomorrow',
'Speed Duel: Arena of Lost Souls',
'Speed Duel: Attack from the Deep',
'Speed Duel: Scars of Battle',
'Speed Duel Starter Decks: Ultimate Predators',
'Speed Duel: Trials of the Kingdom',
'Speed Duel Starter Decks: Match of the Millennium',
'Speed Duel Starter Decks: Twisted Nightmares',
'Speed Duel: Battle City Box',
'Speed Duel GX: Duel Academy Box']
#SpeedDuelProducts=['Speed Duel Starter Decks: Twisted Nightmares']
#setname='Speed Duel Starter Decks: Twisted Nightmares'
#myCards=YugiohSet('yugioh.json')
#setname='Speed Duel Starter Decks: Destiny Masters'
for setname in SpeedDuelProducts:
    cards=f'cardset={setname}'
    csvname=''.join(char for char in setname if char.isalnum())
    jsonName=csvname
    get_online_data(cards,jsonName)
    try: 
        with open(f'{jsonName}.json') as f:
            response_dict=json.load(f)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        cards_dicts = response_dict['data']

    setCode=[]
    setRarity=[]
    setName=[]
    setPrice=[]
    setId=[]
    for card in cards_dicts:
        for set in range(len(card['card_sets'])):
            if card["card_sets"][set]["set_name"]==setname:           
                setCode.append(card["card_sets"][set]['set_code'])
                setRarity.append(card["card_sets"][set]['set_rarity_code'])
                setName.append(card["card_sets"][set]['set_name'])
                setPrice.append(card["card_sets"][set]['set_price'])
                break
        

    pdObj= pd.DataFrame.from_dict(cards_dicts)
    pdObj['Set Code']=setCode
    pdObj['Set_Rarity']=setRarity
    pdObj['Set_Name']=setName
    pdObj['Set_Price']=setPrice
    del pdObj['card_sets']
    del pdObj['card_images']
    del pdObj['card_prices']


    pdObj.to_csv(f'{csvname}.csv', index=False)
    print(pdObj)
    time.sleep(2)
    