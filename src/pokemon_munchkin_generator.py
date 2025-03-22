from notion_api import NotionAPI
from pokemon_munchkin_card import PokemonMunchkinCard

NOTION_API_KEY = "***REMOVED***"
MUNCHKIN_DATABASE_ID = "1a37727e907e80b6ba2bf257adc9c682" # TODO: change to command line argument

MUNCHKIN_POKEMON_TYPES = {
    "⚪": "Normal",
    "🔥": "FIre",
    "💦": "Water",
    "🌱": "Grass",
    "⚡": "Electric",
    "🧊": "Ice",
    "💪": "Fighting",
    "☠️": "Poison",
    "🌎": "Ground",
    "🪽": "Flying",
    "🔮": "Psychic",
    "🐛": "Bug",
    "🪨": "Rock",
    "👻": "Ghost",
    "🐉": "Dragon",
    "👿": "Dark",
    "🏗️": "Steel",
    "🧚": "Fairy"
}

def main():
    api = NotionAPI(NOTION_API_KEY)
    all_pages = api.get_all_pages_database(MUNCHKIN_DATABASE_ID)

    for page in all_pages:
        munchkin_card = PokemonMunchkinCard(
            card_title = page["properties"]["Name"]["title"][0]["text"]["content"],
            bonus = page["properties"]["Bonus"]["number"],
            description_text = "a",
            ally = 1,
            coins = 500,
            types=[MUNCHKIN_POKEMON_TYPES[pokemon_type["name"]] for pokemon_type in page["properties"]["Typing"]["multi_select"]]
        )
        munchkin_card.create_card()

if __name__ == "__main__":
    main()
