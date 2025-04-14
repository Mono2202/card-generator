from munchkin_card import MunchkinCard
from sprite import Sprite
from text import Text


class PokemonMunchkinCard(MunchkinCard):
    MUNCHKIN_POKEMON_TYPE = "types\\Pokemon_Type_Icon_{pokemon_type}"
    MUNCHKIN_POKEMON_CAN_EVOLVE = "can_evolve\\arrow_2"

    BODY_FONT = "CaslonAntique"
    FONT_COLOR = (67, 27, 21)

    def __init__(self, card_title: str, bonus: int, description_blocks: list, ally: int, coins: int, types: list, dex_number: int, can_evolve: bool):
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

        description_all = ""
        if description_blocks == []:
            description_all = "aaa"
        else:
            for block in description_blocks:
                try:
                    description_all += "•" + block["bulleted_list_item"]["rich_text"][0]["plain_text"] + "                                                    "
                except Exception:
                    ...

        super().__init__(
            card_title=card_title,
            bonus=bonus,
            description_text=description_all,
            bottom_left_text=f"{ally} Ally",
            bottom_right_text=f"{coins} Coins",
            additional_sprites=sprites,
            additional_texts=texts,
            output_name=f"{str(dex_number).zfill(4)}_{card_title}"
        )
         