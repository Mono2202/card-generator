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
        # TODO: add this module to images as well

        try:
            text_font = ImageFont.truetype(self._font_path, self._size)
        except IOError:
            text_font = ImageFont.load_default()

        lines = textwrap.wrap(self._text, width=25)
        text_width = draw_ctx.textlength(lines[0], font=text_font)
        fixed_position = ((image_size[0] - text_width) * self._position_percent[0], image_size[1] * self._position_percent[1])
        for line in lines:
            draw_ctx.text(fixed_position, line, fill=self._color, font=text_font)
            fixed_position = (fixed_position[0], fixed_position[1] + self._size)
