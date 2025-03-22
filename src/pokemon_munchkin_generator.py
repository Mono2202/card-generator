from notion_api import NotionAPI
from pokemon_munchkin_card import PokemonMunchkinCard

NOTION_API_KEY = "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"
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
    # print(all_pages[0])
    for page in all_pages:
        page_properties = page["properties"]
        page_content = api.get_page_content(page["id"])

        munchkin_card = PokemonMunchkinCard(
            card_title = page_properties["Name"]["title"][0]["text"]["content"],
            bonus = page_properties["Bonus"]["number"],
            description_blocks=page_content,
            ally = page_properties["Ally"]["number"],
            coins = page_properties["Coins"]["number"],
            types=[MUNCHKIN_POKEMON_TYPES[pokemon_type["name"]] for pokemon_type in page_properties["Typing"]["multi_select"]],
            dex_number=page_properties["Dex Number"]["number"]
        )
        munchkin_card.create_card()
        return

if __name__ == "__main__":
    main()
