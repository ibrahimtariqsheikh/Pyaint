from .settings import *
from .button import *
from .colorWindow import *
from .theme import *


class ColorGradient(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(ColorGradient, cls).__new__(cls)
        return cls.instance

    def __init__(self):

        self.colorWindow = ColorWindow()
        self.color_gradient_box_one_input_one = 0
        self.color_gradient_box_one_input_two = 0
        self.color_gradient_box_one_input_three = 0
        self.color_gradient_box_two_input_one = 0
        self.color_gradient_box_two_input_two = 0
        self.color_gradient_box_two_input_three = 0
        self.theme = Theme()
        self.color_gradient_display_rect = pygame.Rect(
            self.colorWindow.COLOR_WINDOW_WIDTH + 20,
            self.colorWindow.COLOR_WINDOW_HEIGHT + 75,
            50,
            50,
        )
        self.color_gradient_display_button_rect = pygame.Rect(
            self.colorWindow.color_gradients_rect.x
            + self.colorWindow.color_gradients_rect.w
            - 70,
            self.colorWindow.color_gradients_rect.y + 10,
            60,
            50,
        )

        self.color_gradient_buttons = [
            Button(
                self.colorWindow.color_gradients_rect.x + 65,
                self.colorWindow.color_gradients_rect.y + 35,
                50,
                0,
                WHITE,
                name="ColorGradient",
                text="Color Gradient",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x + 20,
                self.colorWindow.color_gradients_rect.y + 121,
                40,
                0,
                WHITE,
                name="ColorBoxTwo",
                text="Color 2:",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x + 20,
                self.colorWindow.color_gradients_rect.y + 82,
                40,
                0,
                WHITE,
                name="ColorBoxOne",
                text="Color 1:",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x + 70,
                self.colorWindow.color_gradients_rect.y + 70,
                40,
                25,
                WHITE,
                name="ColorGradientBoxOneInputOne",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x + 70 + 40 + 10,
                self.colorWindow.color_gradients_rect.y + 70,
                40,
                25,
                WHITE,
                name="ColorGradientBoxOneInputTwo",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x + 70 + 80 + 20,
                self.colorWindow.color_gradients_rect.y + 70,
                40,
                25,
                WHITE,
                name="ColorGradientBoxOneInputThree",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x + 70,
                self.colorWindow.color_gradients_rect.y + 110,
                40,
                25,
                WHITE,
                name="ColorGradientBoxTwoInputOne",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x + 70 + 40 + 10,
                self.colorWindow.color_gradients_rect.y + 110,
                40,
                25,
                WHITE,
                name="ColorGradientBoxTwoInputTwo",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x + 70 + 80 + 20,
                self.colorWindow.color_gradients_rect.y + 110,
                40,
                25,
                WHITE,
                name="ColorGradientBoxTwoInputThree",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradients_rect.x
                + self.colorWindow.color_gradients_rect.w / 2,
                self.colorWindow.color_gradients_rect.y
                + self.colorWindow.color_gradients_rect.h
                - 67,
                50,
                40,
                WHITE,
                text="Add",
                name="AddToCustomColors",
                shape="rectangleWithBorderRadius",
                font_size=15,
            ),
            Button(
                self.colorWindow.color_gradients_rect.x
                + self.colorWindow.color_gradients_rect.w
                - 125,
                self.colorWindow.color_gradients_rect.y + 10,
                60,
                50,
                BLACK,
                gradient_left_color=BLACK,
                gradient_right_color=BLACK,
                isGradient=True,
                border_color=GRAY,
                name="DisplayColorInColorGradient",
            ),
        ]
        for i in range(4):
            self.color_gradient_buttons.append(
            Button(
                self.colorWindow.color_gradients_rect.x
                + self.colorWindow.color_gradients_rect.w
                - 162 + 35 * i,
                self.colorWindow.color_gradients_rect.y + 70,
                30,
                30,
                WHITE,
                name="gradient"+str(i),
            ))
            self.color_gradient_buttons.append(
            Button(
                self.colorWindow.color_gradients_rect.x
                + self.colorWindow.color_gradients_rect.w
                - 162 + 35 * i,
                self.colorWindow.color_gradients_rect.y + 70,
                10,
                10,
                WHITE,
                name="gradientDel"+str(i),
                image_url="assets/close_color_window.png"
            ))
        for i in range(4):
            self.color_gradient_buttons.append(
            Button(
                self.colorWindow.color_gradients_rect.x
                + self.colorWindow.color_gradients_rect.w
                - 162 + 35 * i,
                self.colorWindow.color_gradients_rect.y + 105,
                30,
                30,
                WHITE,
                name="gradient"+str(i),
            ))
        self.box_one_input_one_index = self.getListIndex("ColorGradientBoxOneInputOne")
        self.box_one_input_two_index = self.getListIndex("ColorGradientBoxOneInputTwo")
        self.box_one_input_three_index = self.getListIndex(
            "ColorGradientBoxOneInputThree"
        )
        self.box_two_input_one_index = self.getListIndex("ColorGradientBoxTwoInputOne")
        self.box_two_input_two_index = self.getListIndex("ColorGradientBoxTwoInputTwo")
        self.box_two_input_three_index = self.getListIndex(
            "ColorGradientBoxTwoInputThree"
        )
        self.color_gradient_display_index = self.getListIndex(
            "DisplayColorInColorGradient"
        )

    def draw_color_gradient_buttons(self, win):
        for button in self.color_gradient_buttons:
            button.draw(win)

    # sets the border color to black if selected and grey if not selected in the input boxes
    def setSelectionBorderColor(self):
        for button in self.color_gradient_buttons:
            if button.name.startswith("ColorGradientBox"):
                if button.selected == True:
                    if self.theme.isLightMode:
                        button.border_color = BLACK
                    else:
                        button.border_color = WHITE
                else:
                    button.border_color = SILVER

    # sets and manages the input values according to the color mixer selected
    # pyaint internally stores color as rgb values, hence we convert the colors accordingly and store them
    def setColorGradientInputValues(self):

        if (
            self.color_gradient_buttons[self.box_one_input_one_index].text
            or self.color_gradient_buttons[self.box_two_input_one_index].text
            or self.color_gradient_buttons[self.box_one_input_two_index].text
            or self.color_gradient_buttons[self.box_two_input_two_index].text
            or self.color_gradient_buttons[self.box_one_input_three_index].text
            or self.color_gradient_buttons[self.box_two_input_three_index].text
        ):
            if self.color_gradient_buttons[self.box_one_input_one_index].text:
                self.color_gradient_box_one_input_one = int(
                    self.color_gradient_buttons[self.box_one_input_one_index].text
                )
            else:
                self.color_gradient_box_one_input_one = 0

            if self.color_gradient_buttons[self.box_one_input_two_index].text:
                self.color_gradient_box_one_input_two = int(
                    self.color_gradient_buttons[self.box_one_input_two_index].text
                )
            else:
                self.color_gradient_box_one_input_two = 0

            if self.color_gradient_buttons[self.box_one_input_three_index].text:
                self.color_gradient_box_one_input_three = int(
                    self.color_gradient_buttons[self.box_one_input_three_index].text
                )
            else:
                self.color_gradient_box_one_input_three = 0

            if self.color_gradient_buttons[self.box_two_input_one_index].text:
                self.color_gradient_box_two_input_one = int(
                    self.color_gradient_buttons[self.box_two_input_one_index].text
                )
            else:
                self.color_gradient_box_two_input_one = 0

            if self.color_gradient_buttons[self.box_two_input_two_index].text:
                self.color_gradient_box_two_input_two = int(
                    self.color_gradient_buttons[self.box_two_input_two_index].text
                )
            else:
                self.color_gradient_box_two_input_two = 0

            if self.color_gradient_buttons[self.box_two_input_three_index].text:
                self.color_gradient_box_two_input_three = int(
                    self.color_gradient_buttons[self.box_two_input_three_index].text
                )
            else:
                self.color_gradient_box_two_input_three = 0

            self.color_gradient_buttons[
                self.color_gradient_display_index
            ].gradient_left_color = (
                int(self.color_gradient_box_one_input_one),
                int(self.color_gradient_box_one_input_two),
                int(self.color_gradient_box_one_input_three),
            )
            self.color_gradient_buttons[
                self.color_gradient_display_index
            ].gradient_right_color = (
                int(self.color_gradient_box_two_input_one),
                int(self.color_gradient_box_two_input_two),
                int(self.color_gradient_box_two_input_three),
            )

    # adds the color to the custom color buttons
    def addToGradientColors(self):
        for btn in self.color_gradient_buttons:
            if btn.name.startswith("gradient") and btn.isGradient == False:
                btn.isGradient = True
                btn.gradient_left_color = (
                    int(self.color_gradient_box_one_input_one),
                    int(self.color_gradient_box_one_input_two),
                    int(self.color_gradient_box_one_input_three))
                btn.gradient_right_color = (
                    int(self.color_gradient_box_two_input_one),
                    int(self.color_gradient_box_two_input_two),
                    int(self.color_gradient_box_two_input_three)
                )
                break

    # gets the list index according to the name
    def getListIndex(self, name):
        count = 0
        for button in self.color_gradient_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1

    def handleColorGradientEvents(self, event):
        self.setSelectionBorderColor()
        if event.type == pygame.KEYDOWN:
            for button in self.color_gradient_buttons:
                if (
                    button.name.startswith("ColorGradientBox")
                    and button.selected == True
                ):
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

                self.setColorGradientInputValues()

    def combineColorGradientColors(self):
        red = (
            self.color_gradient_box_one_input_one
            + self.color_gradient_box_two_input_one
        ) / 2
        green = (
            self.color_gradient_box_one_input_two
            + self.color_gradient_box_two_input_two
        ) / 2
        blue = (
            self.color_gradient_box_one_input_three
            + self.color_gradient_box_two_input_three
        ) / 2
        return (red, green, blue)
