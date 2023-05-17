import genanki
import requests

# URL for AnkiConnect API
anki_connect_url = 'http://localhost:8765'

# Deck name to iterate through (replace 'Deck Name' with your deck name)
deck_name = 'My Croatian Deck'

# Get the deck ID using AnkiConnect
response = requests.get(f'{anki_connect_url}/deckNames')
decks = response.json()['result']
deck_id = None
for deck in decks:
    if deck['name'] == deck_name:
        deck_id = deck['id']
        break

if not deck_id:
    print(f'Deck "{deck_name}" not found.')
    exit()

# Get the cards in the deck using AnkiConnect
response = requests.get(f'{anki_connect_url}/findCards', params={'query': f'deck:"{deck_name}"'})
card_ids = response.json()['result']

# List to store custom-made cards
custom_cards = []

# Iterate through the card IDs and get the card info using AnkiConnect
for card_id in card_ids:
    response = requests.get(f'{anki_connect_url}/cardsInfo', params={'cards': [card_id]})
    card_info = response.json()['result']
    card = card_info[0]
    if card['type'] == 1:  # 1 represents custom-made card type
        custom_cards.append(card)

# Print the information of custom-made cards
for card in custom_cards:
    print(card['question'])
    print(card['answer'])




# import requests

# def get_all_cards(deck_name):
#     url = 'http://localhost:8765'
#     payload = {
#         "action": "findCards",
#         "version": 6,
#         "params": {
#             "query": f'deck:"{deck_name}"',
#         }
#     }

#     response = requests.post(url, json=payload)
#     card_ids = response.json()['result']
    
#     return card_ids

# # Specify the deck name
# deck_name = "Minimal Pairs Deck"

# # Get all the card IDs in the specified deck
# card_ids = get_all_cards(deck_name)

# # Print the card IDs
# print("Card IDs:", card_ids)


# import json
# import requests

# # Set up connection to AnkiConnect
# anki_url = "http://localhost:8765"
# deck_name = "Minimal Pairs Deck"
# model_name = "Basic"
# result = requests.get(anki_url, params={"action": "deckNames"})
# print(result.text)
# deck_id = result.json()["result"].index(deck_name) + 1

# Get card IDs in the deck
# result = requests.get(anki_url, params={"action": "findCards", "query": f"deck:{deck_name}"})
# card_ids = result.json()["result"]

# Get card information for each card ID
# cards = []
# for card_id in card_ids:
#     result = requests.get(anki_url, params={"action": "cardsInfo", "cards": json.dumps([card_id])})
#     card = result.json()["result"][0]
#     fields = card["fields"]
#     # Iterate through the fields and do something with the content
#     for field_name, field_content in fields.items():
#         print(f"Field name: {field_name}")
#         print(f"Field content: {field_content}")
#     cards.append(card)