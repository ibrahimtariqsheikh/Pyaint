from utils import *

WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Pyaint")
STATE = "COLOR"
Change = False
isColorWindow = False
isRGBMode = True
custom_color_count = 0
color_mode_red = 0
color_mode_green = 0
color_mode_blue = 0
COLOR_WINDOW_WIDTH_SIZE = 500
COLOR_WINDOW_HEIGHT_SIZE = 570
COLOR_WINDOW_WIDTH = WIDTH / 2 - COLOR_WINDOW_WIDTH_SIZE / 2
COLOR_WINDOW_HEIGHT = WIDTH / 2 - COLOR_WINDOW_HEIGHT_SIZE / 2

color_mixer_rect = pygame.Rect(
    COLOR_WINDOW_WIDTH + 20, COLOR_WINDOW_HEIGHT + 30, 225, 200
)
color_mode_rect = pygame.Rect(
    COLOR_WINDOW_WIDTH + 20 + color_mixer_rect.w + 10,
    COLOR_WINDOW_HEIGHT + 30,
    225,
    200,
)
color_mode_display_rect = pygame.Rect(
    COLOR_WINDOW_WIDTH + 20 + color_mixer_rect.w + 130,
    COLOR_WINDOW_HEIGHT + 75,
    50,
    50,
)
color_mode_switch_rect = pygame.Rect(
    COLOR_WINDOW_WIDTH + 20 + color_mixer_rect.w + color_mode_rect.w - 10,
    COLOR_WINDOW_HEIGHT + 30,
    50,
    20,
)
color_gradients_rect = pygame.Rect(
    COLOR_WINDOW_WIDTH + 20,
    COLOR_WINDOW_HEIGHT + 40 + color_mixer_rect.h,
    460,
    150,
)
color_pallete_rect = pygame.Rect(
    COLOR_WINDOW_WIDTH + 20,
    COLOR_WINDOW_HEIGHT + 50 + color_mixer_rect.h + color_gradients_rect.h,
    460,
    150,
)


def convert_hsv_to_rgb(H, S, V):
    if H > 360 or H < 0 or S > 100 or S < 0 or V > 100 or V < 0:
        print("The given HSV values are not in valid range")
        return
    s = S / 100
    v = V / 100
    C = s * v
    X = C * (1 - abs(math.fmod(H / 60.0, 2) - 1))
    m = v - C

    if H >= 0 and H < 60:
        r = C
        g = X
        b = 0

    elif H >= 60 and H < 120:
        r = X
        g = C
        b = 0
    elif H >= 120 and H < 180:
        r = 0
        g = C
        b = X
    elif H >= 180 and H < 240:
        r = 0
        g = X
        b = C
    elif H >= 240 and H < 300:
        r = X
        g = 0
        b = C
    else:
        r = C
        g = 0
        b = X
    R = (r + m) * 255
    G = (g + m) * 255
    B = (b + m) * 255
    return (R, G, B)


def init_grid(rows, columns, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(columns):  # use _ when variable is not required
            grid[i].append(color)
    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(
                win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
            )

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, SILVER, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(
                win,
                SILVER,
                (i * PIXEL_SIZE, 0),
                (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT),
            )


def convert_rgb_to_hsv(r, g, b):
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
    return h, s, v


def draw_mouse_position_text(win):
    pos = pygame.mouse.get_pos()
    pos_font = get_font(MOUSE_POSITION_TEXT_SIZE)
    try:
        if not isColorWindow:
            row, col = get_row_col_from_pos(pos)
            text_surface = pos_font.render(str(row) + ", " + str(col), 1, BLACK)
            win.blit(text_surface, (5, HEIGHT - TOOLBAR_HEIGHT))
        else:
            for button in color_window_buttons:
                if not button.hover(pos):
                    continue
                if button.name == "CloseColorWindow":
                    text_surface = pos_font.render("Close Window", 1, BLACK)
                    win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                    break
                if isRGBMode:
                    if button.name == "ColorModeInputOne":
                        text_surface = pos_font.render("Enter Red Value", 1, BLACK)
                        win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                        break
                    if button.name == "ColorModeInputTwo":
                        text_surface = pos_font.render("Enter Green Value", 1, BLACK)
                        win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                        break
                    if button.name == "ColorModeInputThree":
                        text_surface = pos_font.render("Enter Blue Value", 1, BLACK)
                        win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                        break
                else:
                    if button.name == "ColorModeInputOne":
                        text_surface = pos_font.render("Enter Hue Value", 1, BLACK)
                        win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                        break
                    if button.name == "ColorModeInputTwo":
                        text_surface = pos_font.render(
                            "Enter Saturation Value", 1, BLACK
                        )
                        win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                        break
                    if button.name == "ColorModeInputThree":
                        text_surface = pos_font.render("Enter Value", 1, BLACK)
                        win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                        break
                if button.name == "DisplayColorInColorMode":
                    text_surface = pos_font.render("Color Mode Display", 1, BLACK)
                    win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                    break
                if button.name == "AddToCustomColors":
                    text_surface = pos_font.render("Add To Custom Colors", 1, BLACK)
                    win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                    break
                if button.name == "SwitchColorMode":
                    text_surface = pos_font.render("Switch Color Mode", 1, BLACK)
                    win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                    break
    except IndexError:
        for button in buttons:
            if not button.hover(pos):
                continue
            if button.text == "Clear":
                text_surface = pos_font.render("Clear Everything", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.text == "Erase":
                text_surface = pos_font.render("Erase", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "FillBucket":
                text_surface = pos_font.render("Fill Bucket", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Brush":
                text_surface = pos_font.render("Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Change":
                text_surface = pos_font.render("Swap Toolbar", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "ColorWindow":
                text_surface = pos_font.render("Color Properties", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break

            r, g, b = button.color
            text_surface = pos_font.render(
                "( " + str(r) + ", " + str(g) + ", " + str(b) + " )", 1, BLACK
            )

            win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))

        for button in brush_widths:
            if not button.hover(pos):
                continue
            if button.width == size_small:
                text_surface = pos_font.render("Small-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_medium:
                text_surface = pos_font.render("Medium-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_large:
                text_surface = pos_font.render("Large-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break


def draw_color_window(win):
    pygame.draw.rect(
        win,
        (255, 255, 255),
        (
            COLOR_WINDOW_WIDTH,
            COLOR_WINDOW_HEIGHT,
            COLOR_WINDOW_WIDTH_SIZE,
            COLOR_WINDOW_HEIGHT_SIZE,
        ),
        width=0,
    )
    pygame.draw.rect(
        win,
        (0, 0, 0),
        (
            COLOR_WINDOW_WIDTH,
            COLOR_WINDOW_HEIGHT,
            COLOR_WINDOW_WIDTH_SIZE,
            COLOR_WINDOW_HEIGHT_SIZE,
        ),
        width=2,
    )
    pygame.draw.rect(
        win,
        SILVER,
        color_mixer_rect,
        width=2,
        border_radius=10,
    )
    pygame.draw.rect(
        win,
        SILVER,
        color_mode_rect,
        width=2,
        border_radius=10,
    )
    pygame.draw.rect(
        win,
        SILVER,
        color_gradients_rect,
        width=2,
        border_radius=10,
    )
    pygame.draw.rect(
        win,
        SILVER,
        color_pallete_rect,
        width=2,
        border_radius=10,
    )


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    draw_brush_widths(win)
    draw_mouse_position_text(win)

    if isColorWindow:
        draw_color_window(win)
        draw_color_window_buttons(win)
    pygame.display.update()


def draw_color_window_buttons(win):

    for button in color_window_buttons:
        if isRGBMode:
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


def draw_brush_widths(win):
    brush_widths = [
        Button(
            rtb_x - size_small / 2,
            480,
            size_small,
            size_small,
            drawing_color,
            None,
            None,
            "ellipse",
        ),
        Button(
            rtb_x - size_medium / 2,
            510,
            size_medium,
            size_medium,
            drawing_color,
            None,
            None,
            "ellipse",
        ),
        Button(
            rtb_x - size_large / 2,
            550,
            size_large,
            size_large,
            drawing_color,
            None,
            None,
            "ellipse",
        ),
    ]
    for button in brush_widths:
        button.draw(win)
        # Set border colour
        border_color = BLACK
        if button.color == BLACK:
            border_color = GRAY
        else:
            border_color = BLACK
        # Set border width
        border_width = 2
        if (
            (BRUSH_SIZE == 1 and button.width == size_small)
            or (BRUSH_SIZE == 2 and button.width == size_medium)
            or (BRUSH_SIZE == 3 and button.width == size_large)
        ):
            border_width = 4
        else:
            border_width = 2
        # Draw border
        pygame.draw.ellipse(
            win,
            border_color,
            (button.x, button.y, button.width, button.height),
            border_width,
        )  # border


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    if col >= ROWS:
        raise IndexError
    return row, col


def paint_using_brush(row, col, size):
    if isColorWindow == False:
        if BRUSH_SIZE == 1:
            grid[row][col] = drawing_color
        else:  # for values greater than 1
            r = row - BRUSH_SIZE + 1
            c = col - BRUSH_SIZE + 1

            for i in range(BRUSH_SIZE * 2 - 1):
                for j in range(BRUSH_SIZE * 2 - 1):
                    if r + i < 0 or c + j < 0 or r + i >= ROWS or c + j >= COLS:
                        continue
                    grid[r + i][c + j] = drawing_color


# Checks whether the coordinated are within the canvas
def inBounds(row, col):
    if row < 0 or col < 0:
        return 0
    if row >= ROWS or col >= COLS:
        return 0
    return 1


def fill_bucket(row, col, color):

    # Visiting array
    vis = [[0 for i in range(101)] for j in range(101)]

    # Creating queue for bfs
    obj = []

    # Pushing pair of {x, y}
    obj.append([row, col])

    # Marking {x, y} as visited
    vis[row][col] = 1

    # Until queue is empty
    while len(obj) > 0:

        # Extracting front pair
        coord = obj[0]
        x = coord[0]
        y = coord[1]
        preColor = grid[x][y]

        grid[x][y] = color

        # Popping front pair of queue
        obj.pop(0)

        # For Upside Pixel or Cell
        if (
            inBounds(x + 1, y) == 1
            and vis[x + 1][y] == 0
            and grid[x + 1][y] == preColor
        ):
            obj.append([x + 1, y])
            vis[x + 1][y] = 1

        # For Downside Pixel or Cell
        if (
            inBounds(x - 1, y) == 1
            and vis[x - 1][y] == 0
            and grid[x - 1][y] == preColor
        ):
            obj.append([x - 1, y])
            vis[x - 1][y] = 1

        # For Right side Pixel or Cell
        if (
            inBounds(x, y + 1) == 1
            and vis[x][y + 1] == 0
            and grid[x][y + 1] == preColor
        ):
            obj.append([x, y + 1])
            vis[x][y + 1] = 1

        # For Left side Pixel or Cell
        if (
            inBounds(x, y - 1) == 1
            and vis[x][y - 1] == 0
            and grid[x][y - 1] == preColor
        ):
            obj.append([x, y - 1])
            vis[x][y - 1] = 1


run = True

clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_width = 40
button_height = 40

button_y_top_row = HEIGHT - TOOLBAR_HEIGHT - 20 + (button_height) - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT - 20 + (button_height * 2) + 1
button_y_last_row = HEIGHT - TOOLBAR_HEIGHT - 20 + (button_height * 3) + 2
button_space = 42

size_small = 25
size_medium = 35
size_large = 50

rtb_x = WIDTH + RIGHT_TOOLBAR_WIDTH / 2
brush_widths = [
    Button(
        rtb_x - size_small / 2,
        480,
        size_small,
        size_small,
        drawing_color,
        None,
        "ellipse",
    ),
    Button(
        rtb_x - size_medium / 2,
        510,
        size_medium,
        size_medium,
        drawing_color,
        None,
        "ellipse",
    ),
    Button(
        rtb_x - size_large / 2,
        550,
        size_large,
        size_large,
        drawing_color,
        None,
        "ellipse",
    ),
]

# Adding Buttons
buttons = []

for i in range(int(len(COLORS) / 2)):
    buttons.append(
        Button(
            100 + button_space * i,
            button_y_top_row,
            button_width,
            button_height,
            (COLORS[i]),
        )
    )

for i in range(int(len(COLORS) / 2)):
    buttons.append(
        Button(
            100 + button_space * i,
            button_y_bot_row,
            button_width,
            button_height,
            COLORS[i + int(len(COLORS) / 2)],
        )
    )

for i in range(int(len(COLORS) / 2)):
    buttons.append(
        Button(
            100 + button_space * i,
            button_y_last_row,
            button_width,
            button_height,
            WHITE,
            name=f"custom_colors_{i}",
        )
    )

# Right toolbar buttons
# need to add change toolbar button.
for i in range(10):
    if i == 0:
        buttons.append(
            Button(
                WIDTH + button_width / 2,
                (i * button_height) + 5,
                button_width,
                button_height,
                WHITE,
                name="Change",
            )
        )  # Change toolbar buttons
    else:
        buttons.append(
            Button(
                WIDTH + button_width / 2,
                (i * button_height) + 5,
                button_width,
                button_height,
                WHITE,
                "B" + str(i - 1),
                BLACK,
            )
        )  # append tools

buttons.append(
    Button(
        WIDTH - button_space,
        button_y_top_row,
        button_width,
        button_height,
        WHITE,
        "Erase",
        BLACK,
    )
)  # Erase Button
buttons.append(
    Button(
        WIDTH - button_space,
        button_y_bot_row,
        button_width,
        button_height,
        WHITE,
        "Clear",
        BLACK,
    )
)  # Clear Button
buttons.append(
    Button(
        WIDTH - 3 * button_space + 5,
        button_y_top_row,
        button_width - 5,
        button_height - 5,
        name="FillBucket",
        image_url="assets/paint-bucket.png",
    )
)  # FillBucket
buttons.append(
    Button(
        WIDTH - 3 * button_space + 45,
        button_y_top_row,
        button_width - 5,
        button_height - 5,
        name="Brush",
        image_url="assets/paint-brush.png",
    )
)  # Brush
buttons.append(
    Button(
        WIDTH - 3 * button_space + 45,
        button_y_top_row + 45,
        button_width - 5,
        button_height - 5,
        name="ColorWindow",
        image_url="assets/color-window.png",
    )
)  # ColorWindow

color_window_buttons = [
    Button(
        COLOR_WINDOW_WIDTH + COLOR_WINDOW_WIDTH_SIZE - 25 - 5,
        COLOR_WINDOW_HEIGHT + 5,
        25,
        25,
        color=WHITE,
        name="CloseColorWindow",
        image_url="assets/close_color_window.png",
    ),
    Button(
        color_mode_rect.x + 50,
        color_mode_rect.y + 25,
        50,
        0,
        WHITE,
        name="ColorMode",
        text="Color Mode",
        shape="text",
    ),
    Button(
        color_mode_rect.x + 20,
        color_mode_rect.y + 60,
        40,
        0,
        WHITE,
        name="ColorModeInputOneText",
        text="Red:",
        shape="text",
    ),
    Button(
        color_mode_rect.x + 20,
        color_mode_rect.y + 90,
        40,
        0,
        WHITE,
        name="ColorModeInputTwoText",
        text="Green:",
        shape="text",
    ),
    Button(
        color_mode_rect.x + 20,
        color_mode_rect.y + 120,
        40,
        0,
        WHITE,
        name="ColorModeInputThreeText",
        text="Blue:",
        shape="text",
    ),
    Button(
        color_mode_rect.x + 70,
        color_mode_rect.y + 50,
        button_width,
        25,
        WHITE,
        name="ColorModeInputOne",
    ),
    Button(
        color_mode_rect.x + 70,
        color_mode_rect.y + 50 + 25 + 5,
        button_width,
        25,
        WHITE,
        name="ColorModeInputTwo",
    ),
    Button(
        color_mode_rect.x + 70,
        color_mode_rect.y + 50 + 25 + 25 + 10,
        button_width,
        25,
        WHITE,
        name="ColorModeInputThree",
    ),
    Button(
        color_mode_rect.x + color_mode_rect.w / 2 + 30,
        color_mode_rect.y + color_mode_rect.h / 2 - 25,
        50,
        50,
        WHITE,
        name="DisplayColorInColorMode",
    ),
    Button(
        color_mode_rect.x + 20,
        color_mode_rect.y + 60,
        40,
        0,
        WHITE,
        name="ColorModeHueText",
        text="Hue:",
        shape="text",
    ),
    Button(
        color_mode_rect.x + 20,
        color_mode_rect.y + 90,
        40,
        0,
        WHITE,
        name="ColorModeSatText",
        text="Sat:",
        shape="text",
    ),
    Button(
        color_mode_rect.x + 20,
        color_mode_rect.y + 120,
        40,
        0,
        WHITE,
        name="ColorModeValueText",
        text="Value:",
        shape="text",
    ),
    Button(
        color_mode_rect.x + color_mode_rect.w / 2 - 90,
        color_mode_rect.y + color_mode_rect.h - 50,
        180,
        40,
        WHITE,
        text="Add To Custom Colors",
        name="AddToCustomColors",
        shape="rectangleWithBorderRadius",
    ),
    Button(
        color_mode_rect.x + color_mode_rect.w - 70,
        color_mode_rect.y + 10,
        60,
        40,
        WHITE,
        text="Switch",
        name="SwitchColorMode",
        shape="rectangleWithBorderRadius",
    ),
]


draw_button = Button(5, HEIGHT - TOOLBAR_HEIGHT / 2 - 30, 60, 60, drawing_color)
buttons.append(draw_button)

while run:
    clock.tick(FPS)  # limiting FPS to 60 or any other value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user closed the program
            run = False

        if isColorWindow:
            for button in color_window_buttons:
                if (
                    button.name == "ColorModeInputOne"
                    or button.name == "ColorModeInputTwo"
                    or button.name == "ColorModeInputThree"
                ):
                    if button.selected == True:
                        button.border_color = BLACK
                    else:
                        button.border_color = SILVER

            if event.type == pygame.KEYDOWN:
                for color_window_button in color_window_buttons:
                    if (
                        color_window_button.name == "ColorModeInputOne"
                        or color_window_button.name == "ColorModeInputTwo"
                        or color_window_button.name == "ColorModeInputThree"
                    ) and color_window_button.selected == True:
                        if event.key == pygame.K_BACKSPACE:
                            user_input = color_window_button.text
                            user_input = user_input[:-1]
                            color_window_button.text = user_input
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
                        ) and len(color_window_button.text) < 3:
                            user_input = color_window_button.text
                            user_input += event.unicode
                            if isRGBMode:
                                if int(user_input) > 255:
                                    user_input = user_input[:-1]
                            else:
                                if color_window_button.name == "ColorModeInputOne":
                                    if int(user_input) > 360:
                                        user_input = user_input[:-1]
                                if (
                                    color_window_button.name == "ColorModeInputTwo"
                                    or color_window_button.name == "ColorModeInputThree"
                                ):
                                    if int(user_input) > 100:
                                        user_input = user_input[:-1]
                            color_window_button.text = user_input

                    if (
                        color_window_buttons[5].text
                        or color_window_buttons[6].text
                        or color_window_buttons[7].text
                    ):
                        if color_window_buttons[5].text:
                            color_mode_red = int(color_window_buttons[5].text)
                        else:
                            color_mode_red = 0

                        if color_window_buttons[6].text:
                            color_mode_green = int(color_window_buttons[6].text)
                        else:
                            color_mode_green = 0

                        if color_window_buttons[7].text:
                            color_mode_blue = int(color_window_buttons[7].text)
                        else:
                            color_mode_blue = 0

                        if not isRGBMode:
                            converted_color = convert_hsv_to_rgb(
                                color_mode_red, color_mode_green, color_mode_blue
                            )
                            (
                                color_mode_red,
                                color_mode_green,
                                color_mode_blue,
                            ) = converted_color

                        color_window_buttons[8].color = (
                            color_mode_red,
                            color_mode_green,
                            color_mode_blue,
                        )

                draw_color_window_buttons(WIN)

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)

                if STATE == "COLOR":
                    paint_using_brush(row, col, BRUSH_SIZE)

                elif STATE == "FILL":
                    fill_bucket(row, col, drawing_color)

                if isColorWindow:

                    for button in color_window_buttons:
                        if not button.clicked(pos):
                            button.selected = False
                            continue
                        if button.name == "CloseColorWindow":
                            isColorWindow = False
                            break
                        if button.name == "AddToCustomColors":
                            for custom_button in buttons:
                                if (
                                    custom_button.name
                                    == f"custom_colors_{custom_color_count}"
                                ):
                                    custom_color_count = (custom_color_count + 1) % 9
                                    custom_button.color = (
                                        color_mode_red,
                                        color_mode_green,
                                        color_mode_blue,
                                    )
                                    break
                        button.selected = True

                for button in color_window_buttons:
                    if not button.clicked(pos):
                        continue
                    if button.name == "SwitchColorMode":
                        isRGBMode = not isRGBMode
                        color_window_buttons[5].text = ""
                        color_window_buttons[6].text = ""
                        color_window_buttons[7].text = ""
                        break

            except IndexError:

                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        draw_button.color = drawing_color
                        STATE = "COLOR"
                        break

                    if button.name == "FillBucket":
                        STATE = "FILL"
                        break

                    if button.name == "ColorWindow":
                        isColorWindow = not isColorWindow
                        break

                    if button.name == "Change":
                        Change = not Change
                        for i in range(10):
                            if i == 0:
                                buttons.append(
                                    Button(
                                        HEIGHT - 2 * button_width,
                                        (i * button_height) + 5,
                                        button_width,
                                        button_height,
                                        WHITE,
                                        name="Change",
                                    )
                                )
                            else:
                                if Change == False:
                                    buttons.append(
                                        Button(
                                            HEIGHT - 2 * button_width,
                                            (i * button_height) + 5,
                                            button_width,
                                            button_height,
                                            WHITE,
                                            "B" + str(i - 1),
                                            BLACK,
                                        )
                                    )
                                if Change == True:
                                    buttons.append(
                                        Button(
                                            HEIGHT - 2 * button_width,
                                            (i * button_height) + 5,
                                            button_width,
                                            button_height,
                                            WHITE,
                                            "C" + str(i - 1),
                                            BLACK,
                                        )
                                    )
                        break

                    if button.name == "Brush":
                        STATE = "COLOR"
                        break

                    drawing_color = button.color
                    draw_button.color = drawing_color

                    break

                for button in brush_widths:
                    if not button.clicked(pos):
                        continue
                    # set brush width
                    if button.width == size_small:
                        BRUSH_SIZE = 1
                    elif button.width == size_medium:
                        BRUSH_SIZE = 2
                    elif button.width == size_large:
                        BRUSH_SIZE = 3

                    STATE = "COLOR"

    draw(WIN, grid, buttons)

pygame.quit()
