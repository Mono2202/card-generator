import argparse
import pandas as pd
from alive_progress import alive_bar
from templates.pokemon_munchkin_card import PokemonMunchkinCard

DATABASE_PATH = "..\\database\\{database}.csv"

TEMPLATES = {
    "pokemon_munchkin": PokemonMunchkinCard
}

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--template", type=str, required=True, help="Card template to generate")
    args = parser.parse_args()
    return args

def main():
    args = get_arguments()
    card_df = pd.read_csv(DATABASE_PATH.format(database=args.template))

    all_cards = card_df.to_dict("records")
    with alive_bar(len(all_cards)) as loading_bar:
        for card_properties in all_cards:
            card = TEMPLATES[args.template](**card_properties)
            card.create_card()
            loading_bar()

if __name__ == "__main__":
    main()
