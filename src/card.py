from PIL import Image, ImageDraw

class Card():
    CARD_BACKGROUND_PATH = "..\\resources\\cards\\"
    SPRITES_PATH = "..\\resources\\sprites\\" 
    FONTS_PATH = "..\\resources\\fonts\\"
    OUTPUT_PATH = "..\\output\\"

    PNG_FILE_EXTENSION = ".png"

    SPRITE_SIZES = (350, 350)

    def __init__(self, card_background: str, card_title: str, texts: list):
        self._card_background_path = self.CARD_BACKGROUND_PATH + card_background + self.PNG_FILE_EXTENSION
        self._card_title = card_title
        self._card_sprite_path = self.SPRITES_PATH + self._card_title.lower() + self.PNG_FILE_EXTENSION
        self._output_path = self.OUTPUT_PATH + self._card_title.lower() + self.PNG_FILE_EXTENSION
        self._texts = texts

    def create_card(self):
        card_background_image = Image.open(self._card_background_path)

        sprite_image = Image.open(self._card_sprite_path)
        sprite_image.thumbnail(self.SPRITE_SIZES)

        sprite_image_pos = ((card_background_image.width - sprite_image.width) // 2, (card_background_image.height - sprite_image.height) // 2)
        card_background_image.paste(sprite_image, sprite_image_pos, sprite_image.convert("RGBA"))

        card_draw_ctx = ImageDraw.Draw(card_background_image)

        for text in self._texts:
            text.add_text_to_image(card_draw_ctx, card_background_image.size)

        card_background_image.save(self._output_path)
