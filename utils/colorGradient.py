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
        self.theme = Theme()

        self.color_gradient_box_one_input_one = 0
        self.color_gradient_box_one_input_two = 0
        self.color_gradient_box_one_input_three = 0
        self.color_gradient_box_two_input_one = 0
        self.color_gradient_box_two_input_two = 0
        self.color_gradient_box_two_input_three = 0
        self.color_gradient_box_three_input_one = 0
        self.color_gradient_box_three_input_two = ''


        self.color_gradient_buttons = [
            Button(
                self.colorWindow.color_gradient_rect.x + 50,
                self.colorWindow.color_gradient_rect.y + 25,
                50,
                0,
                WHITE,
                name="Color Gradient Text",
                text="Color Gradient",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 20,
                self.colorWindow.color_gradient_rect.y + 95,
                40,
                0,
                WHITE,
                name="ColorBoxTwo",
                text="Color 2:",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 20,
                self.colorWindow.color_gradient_rect.y + 125,
                40,
                0,
                WHITE,
                name="ColorBoxThree",
                text="Opacity:",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 20,
                self.colorWindow.color_gradient_rect.y + 65,
                40,
                0,
                WHITE,
                name="ColorBoxOne",
                text="Color 1:",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 70,
                self.colorWindow.color_gradient_rect.y + 55,
                40,
                25,
                WHITE,
                name="ColorGradientBoxOneInputOne",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 70 + 40 + 10,
                self.colorWindow.color_gradient_rect.y + 55,
                40,
                25,
                WHITE,
                name="ColorGradientBoxOneInputTwo",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 70 + 80 + 20,
                self.colorWindow.color_gradient_rect.y + 55,
                40,
                25,
                WHITE,
                name="ColorGradientBoxOneInputThree",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 70,
                self.colorWindow.color_gradient_rect.y + 85,
                40,
                25,
                WHITE,
                name="ColorGradientBoxTwoInputOne",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 70 + 40 + 10,
                self.colorWindow.color_gradient_rect.y + 85,
                40,
                25,
                WHITE,
                name="ColorGradientBoxTwoInputTwo",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 70 + 80 + 20,
                self.colorWindow.color_gradient_rect.y + 85,
                40,
                25,
                WHITE,
                name="ColorGradientBoxTwoInputThree",
                text="0",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 70,
                self.colorWindow.color_gradient_rect.y + 115,
                40,
                25,
                WHITE,
                name="ColorGradientBoxThreeInputOne",
                text="100",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x + 100,
                self.colorWindow.color_gradient_rect.y + 130,
                40,
                0,
                WHITE,
                name="%percentage",
                text="%",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x
                + self.colorWindow.color_gradient_rect.w
                - 120,
                self.colorWindow.color_gradient_rect.y + 35,
                90,
                80,
                BLACK,
                border_color=GRAY,
                name="DisplayGradientInColorGradient",
            ),
            Button(
                self.colorWindow.color_gradient_rect.x
                + self.colorWindow.color_gradient_rect.w / 2
                + 25,
                self.colorWindow.color_gradient_rect.y
                + self.colorWindow.color_gradient_rect.h / 2
                - 20,
                55,
                45,
                WHITE,
                text="Add",
                name="AddToCustomColors",
                shape="rectangleWithBorderRadius",
                font_size=15,
            ),
        ]

        self.box_one_input_one_index = self.getListIndex("ColorGradientBoxOneInputOne")
        self.box_one_input_two_index = self.getListIndex("ColorGradientBoxOneInputTwo")
        self.box_one_input_three_index = self.getListIndex("ColorGradientBoxOneInputThree")
        self.box_two_input_one_index = self.getListIndex("ColorGradientBoxTwoInputOne")
        self.box_two_input_two_index = self.getListIndex("ColorGradientBoxTwoInputTwo")
        self.box_two_input_three_index = self.getListIndex("ColorGradientBoxTwoInputThree")
        self.box_three_input_one_index = self.getListIndex("ColorGradientBoxThreeInputOne")
        self.color_gradient_display_index = self.getListIndex("DisplayGradientInColorGradient")
        self.box_three_input_one_index = self.getListIndex("percentage")

    def draw_color_gradient_buttons(self, win):
        for button in self.color_gradient_buttons:
            button.draw(win)

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

    def getListIndex(self, name):
        count = 0
        for button in self.color_gradient_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1
