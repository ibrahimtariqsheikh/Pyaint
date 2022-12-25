from .settings import *
from .button import *
from .colorWindow import *
from .theme import *
import math


class ColorMode(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ColorMode, cls).__new__(cls)
        return cls.instance

    def __init__(self):

        self.colorWindow = ColorWindow()

        self.isRGBMode = True
        self.color_mode_input_one = 0
        self.color_mode_input_two = 0
        self.color_mode_input_three = 0
        self.theme = Theme()
        self.color_mode_display_rect = pygame.Rect(
            self.colorWindow.COLOR_WINDOW_WIDTH
            + 20
            + self.colorWindow.color_mixer_rect.w
            + 130,
            self.colorWindow.COLOR_WINDOW_HEIGHT + 75,
            50,
            50,
        )
        self.color_mode_switch_rect = pygame.Rect(
            self.colorWindow.COLOR_WINDOW_WIDTH
            + 20
            + self.colorWindow.color_mixer_rect.w
            + self.colorWindow.color_mode_rect.w
            - 10,
            self.colorWindow.COLOR_WINDOW_HEIGHT + 30,
            50,
            20,
        )

        self.color_mode_buttons = [
            Button(
                self.colorWindow.color_mode_rect.x + 50,
                self.colorWindow.color_mode_rect.y + 25,
                50,
                0,
                WHITE,
                name="ColorMode",
                text="Color Mode",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 20,
                self.colorWindow.color_mode_rect.y + 60,
                40,
                0,
                WHITE,
                name="ColorModeInputOneText",
                text="Red:",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 20,
                self.colorWindow.color_mode_rect.y + 90,
                40,
                0,
                WHITE,
                name="ColorModeInputTwoText",
                text="Green:",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 20,
                self.colorWindow.color_mode_rect.y + 120,
                40,
                0,
                WHITE,
                name="ColorModeInputThreeText",
                text="Blue:",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 70,
                self.colorWindow.color_mode_rect.y + 50,
                40,
                25,
                WHITE,
                name="ColorModeInputOne",
                text="0",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 70,
                self.colorWindow.color_mode_rect.y + 50 + 25 + 5,
                40,
                25,
                WHITE,
                name="ColorModeInputTwo",
                text="0",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 70,
                self.colorWindow.color_mode_rect.y + 50 + 25 + 25 + 10,
                40,
                25,
                WHITE,
                name="ColorModeInputThree",
                text="0",
            ),
            Button(
                self.colorWindow.color_mode_rect.x
                + self.colorWindow.color_mode_rect.w
                - 70,
                self.colorWindow.color_mode_rect.y + 10,
                60,
                50,
                BLACK,
                border_color=GRAY,
                name="DisplayColorInColorMode",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 20,
                self.colorWindow.color_mode_rect.y + 60,
                40,
                0,
                WHITE,
                name="ColorModeHueText",
                text="Hue:",
                shape="text",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 20,
                self.colorWindow.color_mode_rect.y + 90,
                40,
                0,
                WHITE,
                name="ColorModeSatText",
                text="Sat:",
                shape="text",
            ),
            Button(
                self.colorWindow.color_mode_rect.x + 20,
                self.colorWindow.color_mode_rect.y + 120,
                40,
                0,
                WHITE,
                name="ColorModeValueText",
                text="Value:",
                shape="text",
            ),
            Button(
                self.colorWindow.color_mode_rect.x
                + self.colorWindow.color_mode_rect.w / 2
                - 90,
                self.colorWindow.color_mode_rect.y
                + self.colorWindow.color_mode_rect.h
                - 50,
                180,
                40,
                WHITE,
                text="Add To Custom Colors",
                name="AddToCustomColors",
                shape="rectangleWithBorderRadius",
                font_size=15,
            ),
            Button(
                self.colorWindow.color_mode_rect.x
                + self.colorWindow.color_mode_rect.w / 2
                + 30,
                self.colorWindow.color_mode_rect.y
                + self.colorWindow.color_mode_rect.h / 2
                - 15,
                60,
                40,
                WHITE,
                text="Switch",
                name="SwitchColorMode",
                shape="rectangleWithBorderRadius",
                font_size=15,
            ),
        ]
        self.input_one_index = self.getListIndex("ColorModeInputOne")
        self.input_two_index = self.getListIndex("ColorModeInputTwo")
        self.input_three_index = self.getListIndex("ColorModeInputThree")
        self.color_mode_display_index = self.getListIndex("DisplayColorInColorMode")

    def draw_color_mode_buttons(self, win):
        for button in self.color_mode_buttons:
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

    # sets the border color to black if selected and grey if not selected in the input boxes
    def setSelectionBorderColor(self):
        for button in self.color_mode_buttons:
            if button.name.startswith("ColorModeInput"):
                if button.selected == True:
                    if self.theme.isLightMode:
                        button.border_color = BLACK
                    else:
                        button.border_color = WHITE
                else:
                    button.border_color = SILVER

    # sets and manages the input values according to the color mode selected
    # pyaint internally stores color as rgb values, hence we convert the colors accordingly and store them
    def setColorModeInputValues(self):

        if (
            self.color_mode_buttons[self.input_one_index].text
            or self.color_mode_buttons[self.input_two_index].text
            or self.color_mode_buttons[self.input_three_index].text
        ):
            if self.color_mode_buttons[self.input_one_index].text:
                self.color_mode_input_one = int(
                    self.color_mode_buttons[self.input_one_index].text
                )
            else:
                self.color_mode_input_one = 0

            if self.color_mode_buttons[self.input_two_index].text:
                self.color_mode_input_two = int(
                    self.color_mode_buttons[self.input_two_index].text
                )
            else:
                self.color_mode_input_two = 0

            if self.color_mode_buttons[self.input_three_index].text:
                self.color_mode_input_three = int(
                    self.color_mode_buttons[self.input_three_index].text
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

            self.color_mode_buttons[self.color_mode_display_index].color = (
                self.color_mode_input_one,
                self.color_mode_input_two,
                self.color_mode_input_three,
            )

    # adds the color to the custom color buttons
    def addToCustomColors(self, buttons):
        count = 0
        for custom_button in buttons:
            if (
                custom_button.name
                and custom_button.name.startswith("custom_colors")
                and custom_button.color == self.theme.BG_BUTTON
            ):
                new_color = (
                    self.color_mode_input_one,
                    self.color_mode_input_two,
                    self.color_mode_input_three,
                )
                if new_color != self.theme.BG_BUTTON:
                    custom_button.color = new_color
                    COLORS.append(new_color)
                    self.colorWindow.custom_color_count = count
                break
            elif (
                custom_button.name
                == f"custom_colors_{self.colorWindow.custom_color_count}"
                and custom_button.color != self.theme.BG_BUTTON
            ):
                custom_button.isGradient = False
                new_color = (
                    self.color_mode_input_one,
                    self.color_mode_input_two,
                    self.color_mode_input_three,
                )
                if new_color != self.theme.BG_BUTTON:
                    self.colorWindow.custom_color_count = (
                        self.colorWindow.custom_color_count + 1
                    ) % 9
                    custom_button.color = new_color
                    COLORS.append(new_color)
                break
            count += 1

    # switch color mode and set input values according to the one selected
    def switchColorMode(self):
        if self.isRGBMode:
            self.isRGBMode = not self.isRGBMode
            (temp_h, temp_s, temp_v,) = self.convert_rgb_to_hsv(
                self.color_mode_input_one,
                self.color_mode_input_two,
                self.color_mode_input_three,
            )

            self.color_mode_buttons[self.input_one_index].text = str(temp_h)
            self.color_mode_buttons[self.input_two_index].text = str(temp_s)
            self.color_mode_buttons[self.input_three_index].text = str(temp_v)

        else:
            self.isRGBMode = not self.isRGBMode

            self.color_mode_buttons[self.input_one_index].text = str(
                self.color_mode_input_one
            )
            self.color_mode_buttons[self.input_two_index].text = str(
                self.color_mode_input_two
            )
            self.color_mode_buttons[self.input_three_index].text = str(
                self.color_mode_input_three
            )

    # gets the list index according to the name
    def getListIndex(self, name):
        count = 0
        for button in self.color_mode_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1

    def handleColorModeEvents(self, event):
        self.setSelectionBorderColor()
        if event.type == pygame.KEYDOWN:
            for button in self.color_mode_buttons:
                if button.name.startswith("ColorModeInput") and button.selected == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = button.text
                        user_input = user_input[:-1]
                        button.text = user_input
                    elif (
                        event.key == pygame.K_0
                        or event.key == pygame.K_1
                        or event.key == pygame.K_2
                        or event.key == pygame.K_3
                        or event.key == pygame.K_4
                        or event.key == pygame.K_5
                        or event.key == pygame.K_6
                        or event.key == pygame.K_7
                        or event.key == pygame.K_8
                        or event.key == pygame.K_9
                    ) and len(button.text) < 3:
                        user_input = button.text
                        user_input += event.unicode
                        if self.isRGBMode:
                            if int(user_input) > 255:
                                user_input = user_input[:-1]
                        else:
                            if button.name == "ColorModeInputOne":
                                if int(user_input) > 360:
                                    user_input = user_input[:-1]
                            if (
                                button.name == "ColorModeInputTwo"
                                or button.name == "ColorModeInputThree"
                            ):
                                if int(user_input) > 100:
                                    user_input = user_input[:-1]
                        button.text = user_input

                self.setColorModeInputValues()
