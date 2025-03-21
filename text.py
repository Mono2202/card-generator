from PIL import ImageFont
import textwrap

class Text():
    FONTS_PATH = "resources\\fonts\\"

    def __init__(self, text: str, font: str, color: tuple, size: int, position_percent: tuple):
        self._text = text
        self._font_path = self.FONTS_PATH + font + ".ttf"
        self._color = color
        self._size = size
        self._position_percent = position_percent

    def add_text_to_image(self, draw_ctx, image_size: tuple):
        # TODO: add text wrap
        # TODO: add this module to images as well

        try:
            text_font = ImageFont.truetype(self._font_path, self._size)
        except IOError:
            text_font = ImageFont.load_default()

        # lines = textwrap.wrap(self._text, width=20)
        # print(lines)
        # for line in lines:
        text_width = draw_ctx.textlength(self._text, font=text_font)
        text_position = ((image_size[0] - text_width) * self._position_percent[0], image_size[1] * self._position_percent[1])
        draw_ctx.text(text_position, self._text, fill=self._color, font=text_font)
