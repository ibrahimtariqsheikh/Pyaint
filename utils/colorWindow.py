from .settings import *
from .button import *
from .theme import *
from .paletteWindow import *
from .AllPalettes import *
from .Palette import *
from .Grayscale import *


class ColorWindow(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ColorWindow, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.isColorWindow = False
        self.paletteWindow = PaletteWindow()
        self.color_window_palette = None
        self.custom_color_count = 0
        self.grayscalePal = Grayscale()
        self.COLOR_WINDOW_WIDTH_SIZE = 500
        self.COLOR_WINDOW_HEIGHT_SIZE = 570
        self.COLOR_WINDOW_WIDTH = WIDTH / 2 - self.COLOR_WINDOW_WIDTH_SIZE / 2
        self.COLOR_WINDOW_HEIGHT = WIDTH / 2 - self.COLOR_WINDOW_HEIGHT_SIZE / 2
        self.theme = Theme()

        self.color_mixer_rect = pygame.Rect(
            self.COLOR_WINDOW_WIDTH + 20, self.COLOR_WINDOW_HEIGHT + 30, 225, 200
        )

        self.color_mode_rect = pygame.Rect(
            self.COLOR_WINDOW_WIDTH + 20 + self.color_mixer_rect.w + 10,
            self.COLOR_WINDOW_HEIGHT + 30,
            225,
            200,
        )

        self.color_gradients_rect = pygame.Rect(
            self.COLOR_WINDOW_WIDTH + 20,
            self.COLOR_WINDOW_HEIGHT + 40 + self.color_mixer_rect.h,
            460,
            150,
        )
        self.color_pallete_rect = pygame.Rect(
            self.COLOR_WINDOW_WIDTH + 20,
            self.COLOR_WINDOW_HEIGHT
            + 50
            + self.color_mixer_rect.h
            + self.color_gradients_rect.h,
            460,
            150,
        )
        self.color_window_buttons = [
            Button(
                self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_WIDTH_SIZE - 25 - 5,
                self.COLOR_WINDOW_HEIGHT + 5,
                25,
                25,
                color=WHITE,
                name="CloseColorWindow",
                image_url=r"assets/close_color_window.png",
            ),
            Button(
                self.color_pallete_rect.x + self.color_pallete_rect.w / 2 - 75,
                33 * self.COLOR_WINDOW_HEIGHT + 20,
                150,
                40,
                WHITE,
                name="Change Palette",
                text="Change Palette",
                text_color=BLACK,
                shape="rectangleWithBorderRadius",
                font_size=15,
            ),
            Button(
                self.color_pallete_rect.x + self.color_pallete_rect.w / 4 - 75,
                self.color_pallete_rect.y + self.color_pallete_rect.h / 12,
                150,
                40,
                WHITE,
                name="Color Palette Text",
                text="Color Palette",
                text_color=BLACK,
                font_size=18,
                shape=None,
            ),
            Button(
                self.color_pallete_rect.x + self.color_pallete_rect.w * 3 / 4 - 75,
                self.color_pallete_rect.y + self.color_pallete_rect.h / 12,
                150,
                40,
                WHITE,
                name="Greyscale Palette Text",
                text="Greyscale Pallete",
                text_color=BLACK,
                font_size=18,
                shape=None,
            ),
        ]

    def append_palette(self):
        self.color_window_palette = self.paletteWindow.currentPalette * 1
        self.j = 450
        for i in range(9):
            self.color_window_buttons.append(
                Button(
                    self.COLOR_WINDOW_WIDTH + 40 + 21 * i,
                    self.COLOR_WINDOW_HEIGHT + self.j,
                    20,
                    20,
                    self.paletteWindow.AllPal.palettes[
                        self.color_window_palette
                    ].palette[i],
                    name="Pal",
                )
            )
        self.j += 22
        for i in range(9):
            self.color_window_buttons.append(
                Button(
                    self.COLOR_WINDOW_WIDTH + 40 + 21 * i,
                    self.COLOR_WINDOW_HEIGHT + self.j,
                    20,
                    20,
                    self.paletteWindow.AllPal.palettes[
                        self.color_window_palette
                    ].palette[i + 9],
                    name="Pal",
                )
            )
        self.grayscalePal.palette.palette = list(
            self.paletteWindow.AllPal.palettes[self.color_window_palette].palette
        )
        self.j = 450
        for i in range(9):
            y = list(self.grayscalePal.palette.palette[i])
            value = int(0.299 * y[0]) + int(0.587 * y[1]) + int(0.114 * y[2])
            y[0] = value
            y[1] = value
            y[2] = value
            x = tuple(y)
            self.color_window_buttons.append(
                Button(
                    self.COLOR_WINDOW_WIDTH + 270 + 21 * i,
                    self.COLOR_WINDOW_HEIGHT + self.j,
                    20,
                    20,
                    x,
                    name="GS",
                )
            )
        self.j += 22
        for i in range(9):
            y = list(self.grayscalePal.palette.palette[i + 9])
            value = int(0.299 * y[0]) + int(0.587 * y[1]) + int(0.114 * y[2])
            y[0] = value
            y[1] = value
            y[2] = value
            x = tuple(y)
            self.color_window_buttons.append(
                Button(
                    self.COLOR_WINDOW_WIDTH + 270 + 21 * i,
                    self.COLOR_WINDOW_HEIGHT + self.j,
                    20,
                    20,
                    x,
                    name="GS",
                )
            )

    def draw_color_window(self, win):
        pygame.draw.rect(
            win,
            self.theme.BG_COLOR,
            (
                self.COLOR_WINDOW_WIDTH,
                self.COLOR_WINDOW_HEIGHT,
                self.COLOR_WINDOW_WIDTH_SIZE,
                self.COLOR_WINDOW_HEIGHT_SIZE,
            ),
            width=0,
        )
        pygame.draw.rect(
            win,
            self.theme.BORDER_COLOR,
            (
                self.COLOR_WINDOW_WIDTH,
                self.COLOR_WINDOW_HEIGHT,
                self.COLOR_WINDOW_WIDTH_SIZE,
                self.COLOR_WINDOW_HEIGHT_SIZE,
            ),
            width=2,
        )
        pygame.draw.rect(
            win,
            SILVER,
            self.color_mixer_rect,
            width=2,
            border_radius=10,
        )
        pygame.draw.rect(
            win,
            SILVER,
            self.color_mode_rect,
            width=2,
            border_radius=10,
        )
        pygame.draw.rect(
            win,
            SILVER,
            self.color_gradients_rect,
            width=2,
            border_radius=10,
        )

        pygame.draw.rect(
            win,
            SILVER,
            self.color_pallete_rect,
            width=2,
            border_radius=10,
        )

    def draw_color_window_buttons(self, win):
        if self.color_window_palette != self.paletteWindow.currentPalette:
            self.color_window_palette = self.paletteWindow.currentPalette * 1
            y = 0
            self.grayscalePal.palette.palette = list(
                self.paletteWindow.AllPal.palettes[
                    self.paletteWindow.currentPalette
                ].palette
            )
            i = 0
            for button in self.color_window_buttons:
                if button.name.startswith("Pal"):
                    button.color = self.paletteWindow.AllPal.palettes[
                        self.color_window_palette
                    ].palette[i]
                    i = i + 1
                if button.name.startswith("GS"):
                    lis = list(self.grayscalePal.palette.palette[y])
                    value = (
                        int(0.299 * lis[0]) + int(0.587 * lis[1]) + int(0.114 * lis[2])
                    )
                    lis[0] = value
                    lis[1] = value
                    lis[2] = value
                    self.grayscalePal.palette.palette[y] = tuple(lis)
                    button.color = tuple(lis)
                    y = y + 1

        for button in self.color_window_buttons:
            button.draw(win)

    def toggle(self):
        self.isColorWindow = not self.isColorWindow

    # gets the list index according to the name
    def getListIndex(self, name):
        count = 0
        for button in self.color_window_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1
