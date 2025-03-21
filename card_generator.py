from card import Card

def main():
    munchkin_card = Card(
        card_background="munchkin",
        card_title="Bulbasaur",
        title_font="Quasimodo",
        text_font="Quasimodo"
    )

    munchkin_card.create_card()

if __name__ == "__main__":
    main()
