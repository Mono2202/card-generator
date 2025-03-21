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

    munchkin_card = Card(
        card_background="munchkin",
        card_title="Bulbasaur",
        texts=[title_text]
    )

    munchkin_card.create_card()

if __name__ == "__main__":
    main()
