from card import Card
from text import Text

class MunchkinCard(Card):
    MUNCHKING_CARD = "munchkin"

    TITLE_FONT = "Quasimodo"
    BODY_FONT = "CaslonAntique"
    FONT_COLOR = (67, 27, 21)

    def __init__(self, card_title: str, bonus: int, description_text: str, ally: int, coins: int):
        texts = []
        texts.append(Text(
            text=f"+{bonus} Bonus",
            font=self.TITLE_FONT,
            color=self.FONT_COLOR,
            size=17,
            position_percent=(0.5, 0.07)
        ))

        texts.append(Text(
            text=card_title,
            font=self.TITLE_FONT,
            color=self.FONT_COLOR,
            size=30,
            position_percent=(0.5, 0.13)
        ))

        texts.append(Text(
            text=description_text,
            font=self.BODY_FONT,
            color=self.FONT_COLOR,
            size=20,
            position_percent=(0.35, 0.60)
        ))

        texts.append(Text(
            text=f"{ally} Ally",
            font=self.BODY_FONT,
            color=self.FONT_COLOR,
            size=15,
            position_percent=(0.1, 0.9)
        ))

        texts.append(Text(
            text=f"{coins} Coins",
            font=self.BODY_FONT,
            color=self.FONT_COLOR,
            size=15,
            position_percent=(0.9, 0.9)
        ))

        super().__init__(card_background=self.MUNCHKING_CARD, card_title=card_title, texts=texts)
