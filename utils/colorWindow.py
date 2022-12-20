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
                text="0",
            ),
            Button(
                self.color_mode_rect.x + 70,
                self.color_mode_rect.y + 50 + 25 + 5,
                40,
                25,
                WHITE,
                name="ColorModeInputTwo",
                text="0",
            ),
            Button(
                self.color_mode_rect.x + 70,
                self.color_mode_rect.y + 50 + 25 + 25 + 10,
                40,
                25,
                WHITE,
                name="ColorModeInputThree",
                text="0",
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
        self.color_mode_red_index = self.getListIndex("ColorModeInputOne")
        self.color_mode_green_index = self.getListIndex("ColorModeInputTwo")
        self.color_mode_blue_index = self.getListIndex("ColorModeInputThree")
        self.color_mode_display_index = self.getListIndex("DisplayColorInColorMode")

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

    # converts hsv to rgb
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
        return int(round(r, 0)), int(round(g, 0)), int(round(b, 0))

    # converts rgb to hsv
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
        return int(round(h, 0)), int(round(s, 0)), int(round(v, 0))

    # gets the list index according to the name
    def getListIndex(self, name):
        count = 0
        for button in self.color_window_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1

    # sets the border color to black if selected and grey if not selected in the input boxes
    def setSelectionBorderColor(self):
        for button in self.color_window_buttons:
            if (
                button.name == "ColorModeInputOne"
                or button.name == "ColorModeInputTwo"
                or button.name == "ColorModeInputThree"
            ):
                if button.selected == True:
                    button.border_color = BLACK
                else:
                    button.border_color = SILVER

    # sets and manages the input values according to the color mode selected
    # pyaint internally stores color as rgb values, since we convert the colors accordingly and store them
    def setColorModeInputValues(self):

        if (
            self.color_window_buttons[self.color_mode_red_index].text
            or self.color_window_buttons[self.color_mode_green_index].text
            or self.color_window_buttons[self.color_mode_blue_index].text
        ):
            if self.color_window_buttons[self.color_mode_red_index].text:
                self.color_mode_input_one = int(
                    self.color_window_buttons[self.color_mode_red_index].text
                )
            else:
                self.color_mode_input_one = 0

            if self.color_window_buttons[self.color_mode_green_index].text:
                self.color_mode_input_two = int(
                    self.color_window_buttons[self.color_mode_green_index].text
                )
            else:
                self.color_mode_input_two = 0

            if self.color_window_buttons[self.color_mode_blue_index].text:
                self.color_mode_input_three = int(
                    self.color_window_buttons[self.color_mode_blue_index].text
                )
            else:
                self.color_mode_input_three = 0

            if not self.isRGBMode:
                (
                    self.color_mode_input_one,
                    self.color_mode_input_two,
                    self.color_mode_input_three,
                ) = self.convert_hsv_to_rgb(
                    self.color_mode_input_one,
                    self.color_mode_input_two,
                    self.color_mode_input_three,
                )

            self.color_window_buttons[self.color_mode_display_index].color = (
                self.color_mode_input_one,
                self.color_mode_input_two,
                self.color_mode_input_three,
            )

    # adds the color to the custom color buttons
    def addToCustomColors(self, buttons):
        for custom_button in buttons:
            if custom_button.name == f"custom_colors_{self.custom_color_count}":
                self.custom_color_count = (self.custom_color_count + 1) % 9
                custom_button.color = (
                    self.color_mode_input_one,
                    self.color_mode_input_two,
                    self.color_mode_input_three,
                )
                COLORS.append(
                    (
                        self.color_mode_input_one,
                        self.color_mode_input_two,
                        self.color_mode_input_three,
                    )
                )
                break

    # switch color mode and set input values according to the one selected
    def switchColorMode(self):
        if self.isRGBMode:
            self.isRGBMode = not self.isRGBMode
            (temp_h, temp_s, temp_v,) = self.convert_rgb_to_hsv(
                self.color_mode_input_one,
                self.color_mode_input_two,
                self.color_mode_input_three,
            )

            self.color_window_buttons[self.color_mode_red_index].text = str(temp_h)
            self.color_window_buttons[self.color_mode_green_index].text = str(temp_s)
            self.color_window_buttons[self.color_mode_blue_index].text = str(temp_v)

        else:
            self.isRGBMode = not self.isRGBMode

            self.color_window_buttons[self.color_mode_red_index].text = str(
                self.color_mode_input_one
            )
            self.color_window_buttons[self.color_mode_green_index].text = str(
                self.color_mode_input_two
            )
            self.color_window_buttons[self.color_mode_blue_index].text = str(
                self.color_mode_input_three
            )
