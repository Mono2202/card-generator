from card import Card
from text import Text

TITLE_COLOR = (67, 27, 21)

def main():
    title_text = Text(
        text="Bulbasaur",
        font="Quasimodo",
        color=TITLE_COLOR,
        size=30,
        position_percent=(0.5, 0.1)
    )

    title_text2 = Text(
        text="Bulbasaur ligma sigma skibidi fortnite chamba",
        font="Quasimodo",
        color=TITLE_COLOR,
        size=15,
        position_percent=(0.1, 0.6)
    )

    ally_text = Text(
        text="1 Ally",
        font="Quasimodo",
        color=TITLE_COLOR,
        size=15,
        position_percent=(0.1, 0.9)
    )

    coin_text = Text(
        text="500 Coins",
        font="Quasimodo",
        color=TITLE_COLOR,
        size=15,
        position_percent=(0.9, 0.9)
    )

    munchkin_card = Card(
        card_background="munchkin",
        card_title="Bulbasaur",
        texts=[title_text, title_text2, ally_text, coin_text]
    )

    munchkin_card.create_card()

if __name__ == "__main__":
    main()
