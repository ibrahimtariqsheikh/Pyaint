from .settings import *
from .button import *
from .colorWindow import *
from .theme import *


class ColorMixer(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ColorMixer, cls).__new__(cls)
        return cls.instance

    def __init__(self):

        self.colorWindow = ColorWindow()
        self.color_mixer_box_one_input_one = 0
        self.color_mixer_box_one_input_two = 0
        self.color_mixer_box_one_input_three = 0
        self.color_mixer_box_two_input_one = 0
        self.color_mixer_box_two_input_two = 0
        self.color_mixer_box_two_input_three = 0
        self.theme = Theme()
        self.color_mixer_display_rect = pygame.Rect(
            self.colorWindow.COLOR_WINDOW_WIDTH + 20,
            self.colorWindow.COLOR_WINDOW_HEIGHT + 75,
            50,
            50,
        )

        self.color_mixer_buttons = [
            Button(
                self.colorWindow.color_mixer_rect.x + 50,
                self.colorWindow.color_mixer_rect.y + 25,
                50,
                0,
                WHITE,
                name="ColorMixer",
                text="Color Mixer",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x + 20,
                self.colorWindow.color_mixer_rect.y + 120,
                40,
                0,
                WHITE,
                name="ColorBoxTwo",
                text="Color 2:",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x + 20,
                self.colorWindow.color_mixer_rect.y + 90,
                40,
                0,
                WHITE,
                name="ColorBoxOne",
                text="Color 1:",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x + 70,
                self.colorWindow.color_mixer_rect.y + 80,
                40,
                25,
                WHITE,
                name="ColorMixerBoxOneInputOne",
                text="0",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x + 70 + 40 + 10,
                self.colorWindow.color_mixer_rect.y + 80,
                40,
                25,
                WHITE,
                name="ColorMixerBoxOneInputTwo",
                text="0",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x + 70 + 80 + 20,
                self.colorWindow.color_mixer_rect.y + 80,
                40,
                25,
                WHITE,
                name="ColorMixerBoxOneInputThree",
                text="0",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x + 70,
                self.colorWindow.color_mixer_rect.y + 110,
                40,
                25,
                WHITE,
                name="ColorMixerBoxTwoInputOne",
                text="0",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x + 70 + 40 + 10,
                self.colorWindow.color_mixer_rect.y + 110,
                40,
                25,
                WHITE,
                name="ColorMixerBoxTwoInputTwo",
                text="0",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x + 70 + 80 + 20,
                self.colorWindow.color_mixer_rect.y + 110,
                40,
                25,
                WHITE,
                name="ColorMixerBoxTwoInputThree",
                text="0",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x
                + self.colorWindow.color_mixer_rect.w
                - 70,
                self.colorWindow.color_mixer_rect.y + 10,
                60,
                50,
                BLACK,
                border_color=GRAY,
                name="DisplayColorInColorMixer",
            ),
            Button(
                self.colorWindow.color_mixer_rect.x
                + self.colorWindow.color_mixer_rect.w / 2
                - 90,
                self.colorWindow.color_mixer_rect.y
                + self.colorWindow.color_mixer_rect.h
                - 50,
                180,
                40,
                WHITE,
                text="Add To Custom Colors",
                name="AddToCustomColors",
                shape="rectangleWithBorderRadius",
                font_size=15,
            ),
        ]
        self.box_one_input_one_index = self.getListIndex("ColorMixerBoxOneInputOne")
        self.box_one_input_two_index = self.getListIndex("ColorMixerBoxOneInputTwo")
        self.box_one_input_three_index = self.getListIndex("ColorMixerBoxOneInputThree")
        self.box_two_input_one_index = self.getListIndex("ColorMixerBoxTwoInputOne")
        self.box_two_input_two_index = self.getListIndex("ColorMixerBoxTwoInputTwo")
        self.box_two_input_three_index = self.getListIndex("ColorMixerBoxTwoInputThree")
        self.color_mixer_display_index = self.getListIndex("DisplayColorInColorMixer")

    def draw_color_mixer_buttons(self, win):
        for button in self.color_mixer_buttons:
            button.draw(win)

    # sets the border color to black if selected and grey if not selected in the input boxes
    def setSelectionBorderColor(self):
        for button in self.color_mixer_buttons:
            if button.name.startswith("ColorMixerBox"):
                if button.selected == True:
                    if self.theme.isLightMode:
                        button.border_color = BLACK
                    else:
                        button.border_color = WHITE
                else:
                    button.border_color = SILVER

    # sets and manages the input values according to the color mixer selected
    # pyaint internally stores color as rgb values, hence we convert the colors accordingly and store them
    def setColorMixerInputValues(self):

        if (
            self.color_mixer_buttons[self.box_one_input_one_index].text
            or self.color_mixer_buttons[self.box_two_input_one_index].text
            or self.color_mixer_buttons[self.box_one_input_two_index].text
            or self.color_mixer_buttons[self.box_two_input_two_index].text
            or self.color_mixer_buttons[self.box_one_input_three_index].text
            or self.color_mixer_buttons[self.box_two_input_three_index].text
        ):
            if self.color_mixer_buttons[self.box_one_input_one_index].text:
                self.color_mixer_box_one_input_one = int(
                    self.color_mixer_buttons[self.box_one_input_one_index].text
                )
            else:
                self.color_mixer_box_one_input_one = 0

            if self.color_mixer_buttons[self.box_one_input_two_index].text:
                self.color_mixer_box_one_input_two = int(
                    self.color_mixer_buttons[self.box_one_input_two_index].text
                )
            else:
                self.color_mixer_box_one_input_two = 0

            if self.color_mixer_buttons[self.box_one_input_three_index].text:
                self.color_mixer_box_one_input_three = int(
                    self.color_mixer_buttons[self.box_one_input_three_index].text
                )
            else:
                self.color_mixer_box_one_input_three = 0

            if self.color_mixer_buttons[self.box_two_input_one_index].text:
                self.color_mixer_box_two_input_one = int(
                    self.color_mixer_buttons[self.box_two_input_one_index].text
                )
            else:
                self.color_mixer_box_two_input_one = 0

            if self.color_mixer_buttons[self.box_two_input_two_index].text:
                self.color_mixer_box_two_input_two = int(
                    self.color_mixer_buttons[self.box_two_input_two_index].text
                )
            else:
                self.color_mixer_box_two_input_two = 0

            if self.color_mixer_buttons[self.box_two_input_three_index].text:
                self.color_mixer_box_two_input_three = int(
                    self.color_mixer_buttons[self.box_two_input_three_index].text
                )
            else:
                self.color_mixer_box_two_input_three = 0

            self.color_mixer_buttons[
                self.color_mixer_display_index
            ].color = self.combineColorMixerColors()

    # adds the color to the custom color buttons
    def addToCustomColors(self, buttons):
        for custom_button in buttons:
            if (
                custom_button.name
                == f"custom_colors_{self.colorWindow.custom_color_count}"
            ):
                self.colorWindow.custom_color_count = (
                    self.colorWindow.custom_color_count + 1
                ) % 9

                custom_button.color = self.combineColorMixerColors()
                COLORS.append(custom_button.color)
                break

    # gets the list index according to the name
    def getListIndex(self, name):
        count = 0
        for button in self.color_mixer_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1

    def handleColorMixerEvents(self, event):
        self.setSelectionBorderColor()
        if event.type == pygame.KEYDOWN:
            for button in self.color_mixer_buttons:
                if button.name.startswith("ColorMixerBox") and button.selected == True:
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
                        if int(user_input) > 255:
                            user_input = user_input[:-1]
                        button.text = user_input

                self.setColorMixerInputValues()

    def combineColorMixerColors(self):
        red = (
            self.color_mixer_box_one_input_one + self.color_mixer_box_two_input_one
        ) / 2
        green = (
            self.color_mixer_box_one_input_two + self.color_mixer_box_two_input_two
        ) / 2
        blue = (
            self.color_mixer_box_one_input_three + self.color_mixer_box_two_input_three
        ) / 2
        return (red, green, blue)
