from .settings import *
from .button import *
import math


class ColorWindow:
    def __init__(self):
        self.isColorWindow = False
        self.isRGBMode = True
        self.custom_color_count = 0
        self.color_mode_input_one = 0
        self.color_mode_input_two = 0
        self.color_mode_input_three = 0
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

        self.color_mode_display_rect = pygame.Rect(
            self.COLOR_WINDOW_WIDTH + 20 + self.color_mixer_rect.w + 130,
            self.COLOR_WINDOW_HEIGHT + 75,
            50,
            50,
        )

        self.color_mode_switch_rect = pygame.Rect(
            self.COLOR_WINDOW_WIDTH
            + 20
            + self.color_mixer_rect.w
            + self.color_mode_rect.w
            - 10,
            self.COLOR_WINDOW_HEIGHT + 30,
            50,
            20,
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
                image_url="assets/close_color_window.png",
            ),
            Button(
                self.color_mode_rect.x + 50,
                self.color_mode_rect.y + 25,
                50,
                0,
                WHITE,
                name="ColorMode",
                text="Color Mode",
            ),
            Button(
                self.color_mode_rect.x + 20,
                self.color_mode_rect.y + 60,
                40,
                0,
                WHITE,
                name="ColorModeInputOneText",
                text="Red:",
            ),
            Button(
                self.color_mode_rect.x + 20,
                self.color_mode_rect.y + 90,
                40,
                0,
                WHITE,
                name="ColorModeInputTwoText",
                text="Green:",
            ),
            Button(
                self.color_mode_rect.x + 20,
                self.color_mode_rect.y + 120,
                40,
                0,
                WHITE,
                name="ColorModeInputThreeText",
                text="Blue:",
            ),
            Button(
                self.color_mode_rect.x + 70,
                self.color_mode_rect.y + 50,
                40,
                25,
                WHITE,
                name="ColorModeInputOne",
            ),
            Button(
                self.color_mode_rect.x + 70,
                self.color_mode_rect.y + 50 + 25 + 5,
                40,
                25,
                WHITE,
                name="ColorModeInputTwo",
            ),
            Button(
                self.color_mode_rect.x + 70,
                self.color_mode_rect.y + 50 + 25 + 25 + 10,
                40,
                25,
                WHITE,
                name="ColorModeInputThree",
            ),
            Button(
                self.color_mode_rect.x + self.color_mode_rect.w / 2 + 30,
                self.color_mode_rect.y + self.color_mode_rect.h / 2 - 25,
                60,
                50,
                BLACK,
                border_color=DARKGRAY,
                name="DisplayColorInColorMode",
            ),
            Button(
                self.color_mode_rect.x + 20,
                self.color_mode_rect.y + 60,
                40,
                0,
                WHITE,
                name="ColorModeHueText",
                text="Hue:",
                shape="text",
            ),
            Button(
                self.color_mode_rect.x + 20,
                self.color_mode_rect.y + 90,
                40,
                0,
                WHITE,
                name="ColorModeSatText",
                text="Sat:",
                shape="text",
            ),
            Button(
                self.color_mode_rect.x + 20,
                self.color_mode_rect.y + 120,
                40,
                0,
                WHITE,
                name="ColorModeValueText",
                text="Value:",
                shape="text",
            ),
            Button(
                self.color_mode_rect.x + self.color_mode_rect.w / 2 - 90,
                self.color_mode_rect.y + self.color_mode_rect.h - 50,
                180,
                40,
                WHITE,
                text="Add To Custom Colors",
                name="AddToCustomColors",
                shape="rectangleWithBorderRadius",
            ),
            Button(
                self.color_mode_rect.x + self.color_mode_rect.w - 70,
                self.color_mode_rect.y + 10,
                60,
                40,
                WHITE,
                text="Switch",
                name="SwitchColorMode",
                shape="rectangleWithBorderRadius",
            ),
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
            if self.isRGBMode:
                if (
                    button.name == "ColorModeHueText"
                    or button.name == "ColorModeSatText"
                    or button.name == "ColorModeValueText"
                ):
                    continue
            else:
                if (
                    button.name == "ColorModeInputOneText"
                    or button.name == "ColorModeInputTwoText"
                    or button.name == "ColorModeInputThreeText"
                ):
                    continue

            button.draw(win)

    def convert_hsv_to_rgb(self, h, s, v):

        temp_saturation = s / 100
        temp_value = v / 100
        C = temp_saturation * temp_value
        X = C * (1 - abs(math.fmod(h / 60.0, 2) - 1))
        m = temp_value - C

        if h >= 0 and h < 60:
            temp_red = C
            temp_green = X
            temp_blue = 0

        elif h >= 60 and h < 120:
            temp_red = X
            temp_green = C
            temp_blue = 0
        elif h >= 120 and h < 180:
            temp_red = 0
            temp_green = C
            temp_blue = X
        elif h >= 180 and h < 240:
            temp_red = 0
            temp_green = X
            temp_blue = C
        elif h >= 240 and h < 300:
            temp_red = X
            temp_green = 0
            temp_blue = C
        else:
            temp_red = C
            temp_green = 0
            temp_blue = X
        r = (temp_red + m) * 255
        g = (temp_green + m) * 255
        b = (temp_blue + m) * 255
        return r, g, b

    def convert_rgb_to_hsv(self, r, g, b):
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx - mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g - b) / df) + 360) % 360
        elif mx == g:
            h = (60 * ((b - r) / df) + 120) % 360
        elif mx == b:
            h = (60 * ((r - g) / df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df / mx) * 100
        v = mx * 100
        return int(h), int(s), int(v)

    def getListIndex(self, name):
        count = 0
        for button in self.color_window_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1
