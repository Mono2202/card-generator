from notion_api import NotionAPI
from munchkin_card import MunchkinCard

NOTION_API_KEY = "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"
MUNCHKIN_DATABASE_ID = "1a37727e907e80b6ba2bf257adc9c682" # TODO: change to command line argument

def main():
    api = NotionAPI(NOTION_API_KEY)
    all_pages = api.get_all_pages_database(MUNCHKIN_DATABASE_ID)

    for page in all_pages:
        munchkin_card = MunchkinCard(
            card_title = page["properties"]["Name"]["title"][0]["text"]["content"],
            bonus = page["properties"]["Bonus"]["number"],
            description_text = "a",
            ally = 1,
            coins = 500
        )
        munchkin_card.create_card()

if __name__ == "__main__":
    main()
