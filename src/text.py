from PIL import ImageFont
import textwrap

class Text():
    FONTS_PATH = "..\\resources\\fonts\\"

    FONT_FILE_EXTENSION = ".ttf"

    def __init__(self, text: str, font: str, color: tuple, size: int, position_percent: tuple):
        self._text = text
        self._font_path = self.FONTS_PATH + font + self.FONT_FILE_EXTENSION
        self._color = color
        self._size = size
        self._position_percent = position_percent

    def add_text_to_image(self, draw_ctx, image_size: tuple):
        try:
            text_font = ImageFont.truetype(self._font_path, self._size)
        except IOError:
            text_font = ImageFont.load_default()

        # TODO: width should be an input
        lines = textwrap.wrap(self._text, width=40)
        text_width = draw_ctx.textlength(lines[0], font=text_font)

        if self._position_percent[0] < 1:
            fixed_position_x = int((image_size[0] - text_width) * self._position_percent[0])
        else:
            fixed_position_x = self._position_percent[0]
        if self._position_percent[1] < 1:
            fixed_position_y = int(image_size[1] * self._position_percent[1])
        else:
            fixed_position_y = self._position_percent[1]
        fixed_position = (fixed_position_x, fixed_position_y)

        for line in lines:
            # title_index = line.find(": ")
            # if title_index >= 0:
            #     draw_ctx.text(fixed_position, line[:title_index + 1], fill=self._color, font=text_font, stroke_width=1, stroke_fill="black")
            #     fixed_position = (fixed_position[0] + len(line[:title_index + 1]), fixed_position[1])
            #     line = line[title_index + 1:]
            draw_ctx.text(fixed_position, line, fill=self._color, font=text_font)
            fixed_position = (fixed_position[0], fixed_position[1] + self._size)
