from .settings import *
from .button import *


class Theme(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Theme, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.isLightMode = True
        self.BG_COLOR = WHITE
        self.BORDER_COLOR = BLACK
        self.BG_TEXTCOLOR = BLACK
        self.DARK_THEME_COLOR = (15, 15, 15)
        self.DARK_THEME_TEXT_BACKGROUND_COLOR = (81, 81, 81)

    def toggle(self, buttons, colorModeButtons, colorWindowButtons, custom_color_count, paletteWindowButtons):
        if self.isLightMode:
            self.BG_COLOR = self.DARK_THEME_COLOR
            self.BG_TEXTCOLOR = WHITE
            count = 0
            for button in buttons:
                button.border_color = WHITE
                if button.name and button.name.startswith("custom_colors_"):
                    count = count + 1
                    if count > custom_color_count:
                        button.color = BLACK
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
            for button in colorModeButtons:
                button.border_color = WHITE
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
            for button in colorWindowButtons:
                button.border_color = WHITE
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE
            for button in paletteWindowButtons:
                button.border_color = WHITE
                if button.text:
                    button.color = self.DARK_THEME_TEXT_BACKGROUND_COLOR
                    button.text_color = WHITE

        else:
            self.BG_COLOR = WHITE
            self.BG_TEXTCOLOR = BLACK
            count = 0
            for button in buttons:
                button.border_color = BLACK
                if button.name and button.name.startswith("custom_colors_"):
                    count = count + 1
                    if count > custom_color_count:
                        button.color = WHITE
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
            for button in colorModeButtons:
                if button.color == BLACK:
                    button.border_color = GRAY
                else:
                    button.border_color = BLACK
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
            for button in colorWindowButtons:
                button.border_color = BLACK
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK
            for button in paletteWindowButtons:
                button.border_color = BLACK
                if button.text:
                    button.color = WHITE
                    button.text_color = BLACK

        self.isLightMode = not self.isLightMode
