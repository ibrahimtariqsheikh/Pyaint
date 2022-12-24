from .settings import *
from .button import *


class ColorPicker(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ColorPicker, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.isColorPicker = False

    # returns the picked color
    def picker(self, win):
        color = tuple(
            win.get_at(pygame.mouse.get_pos())
        )  # get the color of pixel at mouse position
        drawing_color = (color[0], color[1], color[2])
        return drawing_color

    def toggle(self, state):
        if not self.isColorPicker:
            state = "PICKER"
            self.isColorPicker = True
        else:
            state = "COLOR"
            self.isColorPicker = False
        return state

    def draw_zoom_feature_for_color_picker(self, win):
        color = tuple(
            win.get_at(pygame.mouse.get_pos())
        )  # get the color of pixel at mouse position
        current_color = (color[0], color[1], color[2])

        pos = pygame.mouse.get_pos()
        color_picker_button = Button(
            pos[0] + 10,
            pos[1] - 60,
            50,
            50,
            current_color,
            None,
            None,
            "ellipseWithBorderColor",
            border_color=SILVER,
        )
        color_picker_image = Button(
            pos[0] - 10,
            pos[1] - 20,
            25,
            25,
            name="Picker",
            image_url="assets/paint-picker.png",
        )
        color_picker_image.draw(win)
        color_picker_button.draw(win)
