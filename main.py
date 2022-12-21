from utils import *

WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))
colorWindow = ColorWindow()
colorMode = ColorMode()
pygame.display.set_caption("Pyaint")
STATE = "COLOR"
Change = False


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


def draw_mouse_position_text(win):
    pos = pygame.mouse.get_pos()
    pos_font = get_font(MOUSE_POSITION_TEXT_SIZE)
    try:
        if not colorWindow.isColorWindow:
            row, col = get_row_col_from_pos(pos)
            text_surface = pos_font.render(str(row) + ", " + str(col), 1, BLACK)
            win.blit(text_surface, (5, HEIGHT - TOOLBAR_HEIGHT))
        else:
            for button in colorWindow.color_window_buttons:
                if not button.hover(pos):
                    continue
                if button.name == "CloseColorWindow":
                    text_surface = pos_font.render("Close Window", 1, BLACK)
                    win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                    break
            for button in colorMode.color_mode_buttons:
                if not button.hover(pos):
                    continue
                if colorMode.isRGBMode:
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


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    draw_brush_widths(win)
    draw_mouse_position_text(win)

    if colorWindow.isColorWindow:
        colorWindow.draw_color_window(win)
        colorWindow.draw_color_window_buttons(win)
        colorMode.draw_color_mode_buttons(win)
    pygame.display.update()


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
    if colorWindow.isColorWindow == False:
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


def picker():
    '''
    returns the picked color
    '''
    color = tuple(WIN.get_at(pygame.mouse.get_pos())) # get the color of pixel at mouse position
    drawing_color= (color[0],color[1],color[2])
    return drawing_color

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
        image_url=r"assets\paint-bucket.png",
    )
)  # FillBucket
buttons.append(
    Button(
        WIDTH - 3 * button_space + 45,
        button_y_top_row,
        button_width - 5,
        button_height - 5,
        name="Brush",
        image_url=r"assets\paint-brush.png",
    )
)  # Brush
buttons.append(
    Button(
        WIDTH - 3*button_space + 5, 
        button_y_bot_row ,button_width-5, 
        button_height-5, 
        name = "Picker",
        image_url=r"assets/paint-picker.png")
) #Picker

buttons.append(
    Button(
        WIDTH - 3 * button_space + 45,
        button_y_top_row + 45,
        button_width - 5,
        button_height - 5,
        name="ColorWindow",
        image_url=r"assets\color-window.png",
    )
)  # ColorWindow


draw_button = Button(5, HEIGHT - TOOLBAR_HEIGHT / 2 - 30, 60, 60, drawing_color)
buttons.append(draw_button)

while run:
    clock.tick(FPS)  # limiting FPS to 60 or any other value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user closed the program
            run = False

        if colorWindow.isColorWindow:
            colorMode.setSelectionBorderColor()

            if event.type == pygame.KEYDOWN:
                for button in colorMode.color_mode_buttons:
                    if (
                        button.name == "ColorModeInputOne"
                        or button.name == "ColorModeInputTwo"
                        or button.name == "ColorModeInputThree"
                    ) and button.selected == True:
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
                            if colorMode.isRGBMode:
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

                    colorMode.setColorModeInputValues()

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)

                if STATE == "COLOR":
                    paint_using_brush(row, col, BRUSH_SIZE)

                elif STATE == "FILL":
                    fill_bucket(row, col, drawing_color)

                elif STATE == "PICKER":
                    drawing_color = picker()
                    draw_button.color = drawing_color
                    STATE = "COLOR"

                if colorWindow.isColorWindow:

                    for button in colorWindow.color_window_buttons:
                        if not button.clicked(pos):
                            button.selected = False
                            continue
                        if button.name == "CloseColorWindow":
                            colorWindow.isColorWindow = False
                            break
                        button.selected = True

                    for button in colorMode.color_mode_buttons:
                        if not button.clicked(pos):
                            button.selected = False
                            continue
                        if button.name == "AddToCustomColors":
                            colorMode.addToCustomColors(buttons)
                            break
                        if button.name == "SwitchColorMode":
                            colorMode.switchColorMode()
                            break
                        button.selected = True

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

                    if button.name == "Picker":                 
                        STATE = "PICKER"
                        break

                    if button.name == "ColorWindow":
                        colorWindow.isColorWindow = not colorWindow.isColorWindow
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
