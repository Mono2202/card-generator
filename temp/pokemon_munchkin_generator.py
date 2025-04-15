import os.path

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

MUNCHKIN_POKEMON_CAN_EVOLVE = {
    "✅": True,
    "❌": False
}

def main():
    api = NotionAPI(NOTION_API_KEY)
    all_pages = api.get_all_pages_database(MUNCHKIN_DATABASE_ID)
    all_pages.reverse()
    descriptions = []
    for page in all_pages:
        page_properties = page["properties"]
        # if os.path.isfile("..\\output\\" + str(page_properties["Dex Number"]["number"]).zfill(4) + "_" + page_properties["Name"]["title"][0]["text"]["content"].lower() + ".png"):
        #     continue
        page_content = api.get_page_content(page["id"])

        if page_content == []:
            return

        munchkin_card = PokemonMunchkinCard(
            card_title = page_properties["Name"]["title"][0]["text"]["content"],
            bonus = page_properties["Bonus"]["formula"]["number"],
            description_blocks=page_content,
            ally = page_properties["Ally"]["number"],
            coins = page_properties["Coins"]["number"],
            types=[MUNCHKIN_POKEMON_TYPES[pokemon_type["name"]] for pokemon_type in page_properties["Typing"]["multi_select"]],
            dex_number=page_properties["Dex Number"]["number"],
            can_evolve=MUNCHKIN_POKEMON_CAN_EVOLVE[page_properties["Can Evolve"]["select"]["name"]]
        )
        munchkin_card.create_card()

if __name__ == "__main__":
    main()
