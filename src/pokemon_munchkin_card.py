from munchkin_card import MunchkinCard
from sprite import Sprite


class PokemonMunchkinCard(MunchkinCard):
    MUNCHKIN_POKEMON_TYPE = "types\\Pokemon_Type_Icon_{pokemon_type}"

    def __init__(self, card_title: str, bonus: int, description_text: str, ally: int, coins: int, types: list):
        if len(types) == 1:
            x_position_percent = 0.5
            offset = 0
        else:
            x_position_percent = 0.4
            offset = 0.2

        sprites = []
        for pokemon_type in types:
            sprites.append(Sprite(
                sprite=self.MUNCHKIN_POKEMON_TYPE.format(pokemon_type=pokemon_type),
                size=(50, 50),
                position_percent=(x_position_percent, 0.885)
            ))
            x_position_percent += offset
        
        super().__init__(
            card_title=card_title,
            bonus=bonus,
            description_text=description_text,
            bottom_left_text=f"{ally} Ally",
            bottom_right_text=f"{coins} Coins",
            additional_sprites=sprites
        )
         