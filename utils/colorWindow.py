from .settings import *
from .button import *


class ColorWindow(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ColorWindow, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.isColorWindow = False
        self.custom_color_count = 0
        self.COLOR_WINDOW_WIDTH_SIZE = 500
        self.COLOR_WINDOW_HEIGHT_SIZE = 570
        self.COLOR_WINDOW_WIDTH = WIDTH / 2 - self.COLOR_WINDOW_WIDTH_SIZE / 2
        self.COLOR_WINDOW_HEIGHT = WIDTH / 2 - self.COLOR_WINDOW_HEIGHT_SIZE / 2

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
                self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 220,
                33 * self.COLOR_WINDOW_HEIGHT+20,
                45,
                40,
                WHITE,
                name="Change Palette",
                text="Palette",
                text_color=BLACK,
                shape="rectangleWithBorderRadius"
            )
        ]

    def draw_color_window(self, win):
        pygame.draw.rect(
            win,
            (255, 255, 255),
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
            (0, 0, 0),
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
