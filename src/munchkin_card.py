from card import Card
from text import Text
from sprite import Sprite

class MunchkinCard(Card):
    MUNCHKIN_CARD = "munchkin"
    MUNCHKIN_POKEMON_TYPE = "types\\Pokemon_Type_Icon_{pokemon_type}"

    TITLE_FONT = "Quasimodo"
    BODY_FONT = "CaslonAntique"
    FONT_COLOR = (67, 27, 21)

    def __init__(self, card_title: str, bonus: int, description_text: str, ally: int, coins: int, types: list):
        texts = []
        texts.append(Text(
            text=f"+{bonus} Bonus",
            font=self.TITLE_FONT,
            color=self.FONT_COLOR,
            size=34,
            position_percent=(0.5, 0.07)
        ))

        texts.append(Text(
            text=card_title,
            font=self.TITLE_FONT,
            color=self.FONT_COLOR,
            size=60,
            position_percent=(0.5, 0.13)
        ))

        texts.append(Text(
            text=description_text,
            font=self.BODY_FONT,
            color=self.FONT_COLOR,
            size=40,
            position_percent=(0.35, 0.60)
        ))

        texts.append(Text(
            text=f"{ally} Ally",
            font=self.BODY_FONT,
            color=self.FONT_COLOR,
            size=30,
            position_percent=(0.1, 0.9)
        ))

        texts.append(Text(
            text=f"{coins} Coins",
            font=self.BODY_FONT,
            color=self.FONT_COLOR,
            size=30,
            position_percent=(0.9, 0.9)
        ))

        sprites = []
        sprites.append(Sprite(
            sprite=card_title,
            size=(425, 425),
            position_percent=(0.5, 0.1)
        ))
        
        # TODO: create pokemon munchkin class
        if len(types) == 1:
            x_position_percent = 0.5
            offset = 0
        else:
            x_position_percent = 0.4
            offset = 0.2
        for pokemon_type in types:
            sprites.append(Sprite(
                sprite=self.MUNCHKIN_POKEMON_TYPE.format(pokemon_type=pokemon_type),
                size=(50, 50),
                position_percent=(x_position_percent, 0.885)
            ))
            x_position_percent += offset

        super().__init__(card_background=self.MUNCHKIN_CARD, output_name=card_title, texts=texts, sprites=sprites)
