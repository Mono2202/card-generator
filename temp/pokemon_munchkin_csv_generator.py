import os
from alive_progress import alive_bar
import pandas as pd
from templates.pokemon_munchkin_card import PokemonMunchkinCard

POKEMON_MUNCHKIN_CSV_PATH = "..\\database\\pokemon_munchkin.csv"

def generate():
    df = pd.read_csv(POKEMON_MUNCHKIN_CSV_PATH)
    all_pokemon = df.to_dict('records')
    with alive_bar(len(all_pokemon)) as bar:
        for pokemon in all_pokemon:
            # TODO: make optional with parseargs
            # if os.path.isfile("..\\output\\" + str(pokemon["Dex Number"]).zfill(4) + "_" + pokemon["Name"].lower() + ".png"):
            #     continue
            munchkin_card = PokemonMunchkinCard(
                card_title = pokemon["Name"],
                bonus = pokemon["Bonus"],
                description=pokemon["Description"],
                ally = pokemon["Ally"],
                coins = pokemon["Coins"],
                types= pokemon["Typing"].split(", "),
                dex_number=pokemon["Dex Number"],
                can_evolve=pokemon["Can Evolve"]
            )
            munchkin_card.create_card()
            bar()
