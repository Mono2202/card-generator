from templates.munchkin_card import MunchkinCard
from card.sprite import Sprite
from card.text import Text


class PokemonMunchkinCard(MunchkinCard):
    MUNCHKIN_POKEMON_TYPE = "types\\Pokemon_Type_Icon_{pokemon_type}"
    MUNCHKIN_POKEMON_CAN_EVOLVE = "can_evolve\\arrow_2"

    BODY_FONT = "CaslonAntique"
    FONT_COLOR = (67, 27, 21)

    def __init__(self, name: str, bonus: int, description: str, ally: int, coins: int, typing: str, dex_number: int, can_evolve: bool, category: str):
        typing = typing.split(", ")
        if len(typing) == 1:
            x_position_percent = 0.5
            offset = 0
        else:
            x_position_percent = 0.4
            offset = 0.2

        sprites = []
        for pokemon_type in typing:
            sprites.append(Sprite(
                sprite=self.MUNCHKIN_POKEMON_TYPE.format(pokemon_type=pokemon_type),
                size=(50, 50),
                position_percent=(x_position_percent, 0.883)
            ))
            x_position_percent += offset

        if can_evolve:
            sprites.append(Sprite(
                sprite=self.MUNCHKIN_POKEMON_CAN_EVOLVE,
                size=(50, 50),
                position_percent=(0.9, 0.048)
            ))
        
        texts = [
            Text(
                text=f"#{dex_number}",
                font=self.BODY_FONT,
                color=self.FONT_COLOR,
                size=30,
                position_percent=(0.1, 0.06)
            )
        ]

        super().__init__(
            card_title=name,
            bonus=bonus,
            # TODO: add dots?
            description_text=description.replace("\n", "                                                    "),
            bottom_left_text=f"{ally} Ally",
            bottom_right_text=f"{coins} Coins",
            additional_sprites=sprites,
            additional_texts=texts,
            output_name=f"{str(dex_number).zfill(4)}_{name}"
        )
         