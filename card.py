from PIL import Image, ImageDraw, ImageFont

class Card():
    CARD_BACKGROUND_PATH = "resources\\cards\\"
    SPRITES_PATH = "resources\\sprites\\" 
    FONTS_PATH = "resources\\fonts\\"
    OUTPUT_PATH = "output\\"

    SPRITE_SIZES = (350, 350)

    WHITE_COLOR = (255, 255, 255)
    TITLE_COLOR = (67, 27, 21)

    def __init__(self, card_background: str, card_title: str, title_font: str, text_font: str):
        self._card_background_path = self.CARD_BACKGROUND_PATH + card_background + ".png"
        self._card_title = card_title
        self._card_sprite_path = self.SPRITES_PATH + self._card_title.lower() + ".png"
        self._output_path = self.OUTPUT_PATH + self._card_title.lower() + ".png"
        self._title_font_path = self.FONTS_PATH + title_font + ".ttf"
        self._text_font_path = self.FONTS_PATH + text_font + ".ttf"

    def create_card(self):
        card_background_image = Image.open(self._card_background_path)

        sprite_image = Image.open(self._card_sprite_path)
        sprite_image.thumbnail(self.SPRITE_SIZES)

        sprite_image_pos = ((card_background_image.width - sprite_image.width) // 2, (card_background_image.height - sprite_image.height) // 2)
        card_background_image.paste(sprite_image, sprite_image_pos, sprite_image.convert("RGBA"))

        card_draw_ctx = ImageDraw.Draw(card_background_image)

        title_font_color = self.TITLE_COLOR
        try:
            title_font = ImageFont.truetype(self._title_font_path, 30)
        except IOError:
            title_font = ImageFont.load_default()
        
        text_width = card_draw_ctx.textlength(self._card_title, font=title_font)
        text_pos = ((card_background_image.width - text_width) // 2, 30)
        card_draw_ctx.text(text_pos, self._card_title, fill=title_font_color, font=title_font)

        card_background_image.save(self._output_path)
