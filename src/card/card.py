from PIL import Image, ImageDraw

class Card():
    CARD_BACKGROUND_PATH = "..\\resources\\cards\\"
    OUTPUT_PATH = "..\\output\\"

    PNG_FILE_EXTENSION = ".png"

    def __init__(self, card_background: str, output_name: str, texts: list, sprites: list):
        self._card_background_path = self.CARD_BACKGROUND_PATH + card_background + self.PNG_FILE_EXTENSION
        self._output_path = self.OUTPUT_PATH + output_name + self.PNG_FILE_EXTENSION
        self._texts = texts
        self._sprites = sprites

    def create_card(self):
        card_background_image = Image.open(self._card_background_path)

        card_draw_ctx = ImageDraw.Draw(card_background_image)

        for text in self._texts:
            text.add_text_to_image(card_draw_ctx, card_background_image.size)

        for sprite in self._sprites:
            sprite.add_sprite_to_image(card_background_image)

        card_background_image.save(self._output_path)
