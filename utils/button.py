from turtle import pos
from .settings import *


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        color=(0, 0, 0),
        text="",
        text_color=BLACK,
        shape="rectangle",
        image_url="/",
        name=None,
        selected=False,
        border_color=BLACK,
        border_width=0,
        font_size=None,
        isGradient=False,
        gradient_left_color=BLACK,
        gradient_right_color=BLACK,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.shape = shape
        self.text_color = text_color
        self.image_url = image_url
        self.name = name
        self.selected = selected
        self.border_color = border_color
        self.border_width = border_width
        self.font_size = font_size
        self.isGradient = isGradient
        self.gradient_left_color = (gradient_left_color,)
        self.gradient_right_color = (gradient_right_color,)

    def draw(self, win):

        if self.isGradient:
            colour_rect = pygame.Surface((2, 2))
            pygame.draw.line(colour_rect, self.gradient_left_color, (0, 0), (0, 1))
            pygame.draw.line(colour_rect, self.gradient_right_color, (1, 0), (1, 1))
            colour_rect = pygame.transform.smoothscale(
                colour_rect, (self.width, self.height)
            )
            win.blit(colour_rect, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(
                win, self.border_color, (self.x, self.y, self.width, self.height), 2
            )
        else:
            if self.image_url != "/":
                my_image = pygame.image.load(self.image_url)
                my_image = pygame.transform.scale(my_image, (self.width, self.height))
                win.blit(my_image, (self.x, self.y))

            elif self.shape == "rectangle":
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.width, self.height)
                )
                pygame.draw.rect(
                    win, self.border_color, (self.x, self.y, self.width, self.height), 2
                )

            elif self.shape == "rectangleWithBorderRadius":
                pygame.draw.rect(
                    win, self.color, (self.x, self.y, self.width, self.height)
                )
                pygame.draw.rect(
                    win,
                    self.border_color,
                    (self.x, self.y, self.width, self.height),
                    2,
                    10,
                )

            elif self.shape == "ellipse":
                pygame.draw.ellipse(
                    win,
                    self.color,
                    (self.x, self.y, self.width, self.height),
                    self.border_width,
                )  # fill
                # pygame.draw.ellipse(win, BLACK, (self.x, self.y, self.width, self.height), 2) #border

            elif self.shape == "ellipseWithBorderColor":
                pygame.draw.ellipse(
                    win, self.color, (self.x, self.y, self.width, self.height)
                )  # fill
                pygame.draw.ellipse(
                    win, self.border_color, (self.x, self.y, self.width, self.height), 2
                )  # border

            if self.text:
                if self.font_size:
                    button_font = get_font(self.font_size)
                else:
                    button_font = get_font(int(self.width / 2) - 6)
                text_surface = button_font.render(self.text, 1, self.text_color)
                win.blit(
                    text_surface,
                    (
                        self.x + self.width / 2 - text_surface.get_width() / 2,
                        self.y + self.height / 2 - text_surface.get_height() / 2,
                    ),
                )

    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True

    def hover(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True
