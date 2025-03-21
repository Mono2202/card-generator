from PIL import Image

class Sprite():
    SPRITES_PATH = "..\\resources\\sprites\\" 

    PNG_FILE_EXTENSION = ".png"

    def __init__(self, sprite: str, size: tuple, position_percent: tuple):
        self._sprite_path = self.SPRITES_PATH + sprite + self.PNG_FILE_EXTENSION
        self._size = size
        self._position_percent = position_percent

    def add_sprite_to_image(self, background_image):
        sprite_image = Image.open(self._sprite_path)
        sprite_image.thumbnail(self._size)

        fixed_position = (int((background_image.width - sprite_image.width) * self._position_percent[0]), int(background_image.height * self._position_percent[1]))
        background_image.paste(sprite_image, fixed_position, sprite_image.convert("RGBA"))
