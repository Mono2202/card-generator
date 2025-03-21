from munchking_card import MunchkinCard


def main():
    munchkin_card = MunchkinCard(
        card_title="Bulbasaur",
        description_text="Sigma Pomni Chamnba Ligma",
        ally=1,
        coins=500
    )
    munchkin_card.create_card()

if __name__ == "__main__":
    main()
