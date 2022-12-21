from .settings import *
from .button import *
from .AllPalettes import *

class PaletteWindow:
    def __init__(self):
        self.count=0
        self.isAppend= True
        self.AllPal= AllPalettes()
        self.isPaletteWindow = False
        self.isRGBMode = True
        self.r1 = 0
        self.g1 = 0
        self.b1 = 0
        self.r2 = 0
        self.g2 = 0
        self.b2 = 0
        self.r3 = 0
        self.g3 = 0
        self.b3 = 0
        self.r4 = 0
        self.g4 = 0
        self.b4 = 0
        self.r5 = 0
        self.g5 = 0
        self.b5 = 0
        self.r6 = 0
        self.g6 = 0
        self.b6 = 0
        self.r7 = 0
        self.g7 = 0
        self.b7 = 0
        self.r8 = 0
        self.g8 = 0
        self.b8 = 0
        self.r9 = 0
        self.g9 = 0
        self.b9 = 0
        self.r10 = 0
        self.g10 = 0
        self.b10 = 0
        self.r11 = 0
        self.g11 = 0
        self.b11 = 0
        self.r12 = 0
        self.g12 = 0
        self.b12 = 0
        self.r13 = 0
        self.g13 = 0
        self.b13 = 0
        self.r14 = 0
        self.g14 = 0
        self.b14 = 0
        self.r15 = 0
        self.g15 = 0
        self.b15 = 0
        self.r16 = 0
        self.g16 = 0
        self.b16 = 0
        self.name= ""
        self.rect_x_y = [320,162,363,162,406,162,320,182,363,182,406,182,320,202,363,202,406,202,320,222,363,222,406,222,320,242,363,242,406,242,320,262,363,262,406,262,320,282,363,282,406,282,320,302,363,302,406,302,320,322,363,322,406,322,320,342,363,342,406,342,320,362,363,362,406,362,320,382,363,382,406,382,
                        320,402,363,402,406,402,320,422,363,422,406,422,320,442,363,442,406,442,320,462,363,462,406,462,]
        self.COLOR_WINDOW_SIZE = 400
        self.COLOR_WINDOW_WIDTH = WIDTH / 2 - self.COLOR_WINDOW_SIZE / 2
        self.COLOR_WINDOW_HEIGHT = WIDTH / 2 - self.COLOR_WINDOW_SIZE / 2
        self.palette_window_buttons = [
            Button(
                self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_SIZE - 25 - 5,
                self.COLOR_WINDOW_HEIGHT + 5,
                25,
                25,
                color=WHITE,
                name="ClosePaletteWindow",
                image_url="assets/close_color_window.png",
            ),
            Button(
                self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 130 + 40,
                self.COLOR_WINDOW_HEIGHT+20 * 2,
                80,
                15,
                WHITE,
                name="PaletteName",
            ),
            Button(
                int(self.rect_x_y[0]),
                int(self.rect_x_y[1]),
                40,
                15,
                WHITE,
                name="ColorR1",
            ),
            Button(
                int(self.rect_x_y[2]),
                int(self.rect_x_y[3]),
                40,
                15,
                WHITE,
                name="ColorG1",
            ),
            Button(
                int(self.rect_x_y[4]),
                int(self.rect_x_y[5]),
                40,
                15,
                WHITE,
                name="ColorB1",
            ),
            Button(
                int(self.rect_x_y[6]),
                int(self.rect_x_y[7]),
                40,
                15,
                WHITE,
                name="ColorR2",
            ),
            Button(
                int(self.rect_x_y[8]),
                int(self.rect_x_y[9]),
                40,
                15,
                WHITE,
                name="ColorG2",
            ),
            Button(
                int(self.rect_x_y[10]),
                int(self.rect_x_y[11]),
                40,
                15,
                WHITE,
                name="ColorB2",
            ),
            Button(
                int(self.rect_x_y[12]),
                int(self.rect_x_y[13]),
                40,
                15,
                WHITE,
                name="ColorR3",
            ),
            Button(
                int(self.rect_x_y[14]),
                int(self.rect_x_y[15]),
                40,
                15,
                WHITE,
                name="ColorG3",
            ),
            Button(
                int(self.rect_x_y[16]),
                int(self.rect_x_y[17]),
                40,
                15,
                WHITE,
                name="ColorB3",
            ),
            Button(
                int(self.rect_x_y[18]),
                int(self.rect_x_y[19]),
                40,
                15,
                WHITE,
                name="ColorR4",
            ),
            Button(
                int(self.rect_x_y[20]),
                int(self.rect_x_y[21]),
                40,
                15,
                WHITE,
                name="ColorG4",
            ),
            Button(
                int(self.rect_x_y[22]),
                int(self.rect_x_y[23]),
                40,
                15,
                WHITE,
                name="ColorB4",
            ),
            Button(
                int(self.rect_x_y[24]),
                int(self.rect_x_y[25]),
                40,
                15,
                WHITE,
                name="ColorR5",
            ),
            Button(
                int(self.rect_x_y[26]),
                int(self.rect_x_y[27]),
                40,
                15,
                WHITE,
                name="ColorG5",
            ),
            Button(
                int(self.rect_x_y[28]),
                int(self.rect_x_y[29]),
                40,
                15,
                WHITE,
                name="ColorB5",
            ),
            Button(
                int(self.rect_x_y[30]),
                int(self.rect_x_y[31]),
                40,
                15,
                WHITE,
                name="ColorR6",
            ),
            Button(
                int(self.rect_x_y[32]),
                int(self.rect_x_y[33]),
                40,
                15,
                WHITE,
                name="ColorG6",
            ),
            Button(
                int(self.rect_x_y[34]),
                int(self.rect_x_y[35]),
                40,
                15,
                WHITE,
                name="ColorB6",
            ),
            Button(
                int(self.rect_x_y[36]),
                int(self.rect_x_y[37]),
                40,
                15,
                WHITE,
                name="ColorR7",
            ),
            Button(
                int(self.rect_x_y[38]),
                int(self.rect_x_y[39]),
                40,
                15,
                WHITE,
                name="ColorG7",
            ),
            Button(
                int(self.rect_x_y[40]),
                int(self.rect_x_y[41]),
                40,
                15,
                WHITE,
                name="ColorB7",
            ),
            Button(
                int(self.rect_x_y[42]),
                int(self.rect_x_y[43]),
                40,
                15,
                WHITE,
                name="ColorR8",
            ),
            Button(
                int(self.rect_x_y[44]),
                int(self.rect_x_y[45]),
                40,
                15,
                WHITE,
                name="ColorG8",
            ),
            Button(
                int(self.rect_x_y[46]),
                int(self.rect_x_y[47]),
                40,
                15,
                WHITE,
                name="ColorB8",
            ),
            Button(
                int(self.rect_x_y[48]),
                int(self.rect_x_y[49]),
                40,
                15,
                WHITE,
                name="ColorR9",
            ),
            Button(
                int(self.rect_x_y[50]),
                int(self.rect_x_y[51]),
                40,
                15,
                WHITE,
                name="ColorG9",
            ),
            Button(
                int(self.rect_x_y[52]),
                int(self.rect_x_y[53]),
                40,
                15,
                WHITE,
                name="ColorB9",
            ),
            Button(
                int(self.rect_x_y[54]),
                int(self.rect_x_y[55]),
                40,
                15,
                WHITE,
                name="ColorR10",
            ),
            Button(
                int(self.rect_x_y[56]),
                int(self.rect_x_y[57]),
                40,
                15,
                WHITE,
                name="ColorG10",
            ),
            Button(
                int(self.rect_x_y[58]),
                int(self.rect_x_y[59]),
                40,
                15,
                WHITE,
                name="ColorB10",
            ),
            Button(
                int(self.rect_x_y[60]),
                int(self.rect_x_y[61]),
                40,
                15,
                WHITE,
                name="ColorR11",
            ),
            Button(
                int(self.rect_x_y[62]),
                int(self.rect_x_y[63]),
                40,
                15,
                WHITE,
                name="ColorG11",
            ),
            Button(
                int(self.rect_x_y[64]),
                int(self.rect_x_y[65]),
                40,
                15,
                WHITE,
                name="ColorB11",
            ),
            Button(
                int(self.rect_x_y[66]),
                int(self.rect_x_y[67]),
                40,
                15,
                WHITE,
                name="ColorR12",
            ),
            Button(
                int(self.rect_x_y[68]),
                int(self.rect_x_y[69]),
                40,
                15,
                WHITE,
                name="ColorG12",
            ),
            Button(
                int(self.rect_x_y[70]),
                int(self.rect_x_y[71]),
                40,
                15,
                WHITE,
                name="ColorB12",
            ),
            Button(
                int(self.rect_x_y[72]),
                int(self.rect_x_y[73]),
                40,
                15,
                WHITE,
                name="ColorR13",
            ),
            Button(
                int(self.rect_x_y[74]),
                int(self.rect_x_y[75]),
                40,
                15,
                WHITE,
                name="ColorG13",
            ),
            Button(
                int(self.rect_x_y[76]),
                int(self.rect_x_y[77]),
                40,
                15,
                WHITE,
                name="ColorB13",
            ),
            Button(
                int(self.rect_x_y[78]),
                int(self.rect_x_y[79]),
                40,
                15,
                WHITE,
                name="ColorR14",
            ),
            Button(
                int(self.rect_x_y[80]),
                int(self.rect_x_y[81]),
                40,
                15,
                WHITE,
                name="ColorG14",
            ),
            Button(
                int(self.rect_x_y[82]),
                int(self.rect_x_y[83]),
                40,
                15,
                WHITE,
                name="ColorB14",
            ),
            Button(
                int(self.rect_x_y[84]),
                int(self.rect_x_y[85]),
                40,
                15,
                WHITE,
                name="ColorR15",
            ),
            Button(
                int(self.rect_x_y[86]),
                int(self.rect_x_y[87]),
                40,
                15,
                WHITE,
                name="ColorG15",
            ),
            Button(
                int(self.rect_x_y[88]),
                int(self.rect_x_y[89]),
                40,
                15,
                WHITE,
                name="ColorB15",
            ),
            Button(
                int(self.rect_x_y[90]),
                int(self.rect_x_y[91]),
                40,
                15,
                WHITE,
                name="ColorR16",
            ),
            Button(
                int(self.rect_x_y[92]),
                int(self.rect_x_y[93]),
                40,
                15,
                WHITE,
                name="ColorG16",
            ),
            Button(
                int(self.rect_x_y[94]),
                int(self.rect_x_y[95]),
                40,
                15,
                WHITE,
                name="ColorB16",
            )
        ]

    def draw_palette_window(self, win):
        pygame.draw.rect(
            win,
            (255, 255, 255),
            (
                self.COLOR_WINDOW_WIDTH,
                self.COLOR_WINDOW_HEIGHT,
                self.COLOR_WINDOW_SIZE,
                self.COLOR_WINDOW_SIZE,
            ),
            width=0,
        )
        pygame.draw.rect(
            win,
            (0, 0, 0),
            (
                self.COLOR_WINDOW_WIDTH,
                self.COLOR_WINDOW_HEIGHT,
                self.COLOR_WINDOW_SIZE,
                self.COLOR_WINDOW_SIZE,
            ),
            width=2,
        )

    def palAppend(self):
        self.palette_window_buttons.append(
                        Button(
                        self.COLOR_WINDOW_WIDTH +10,
                        self.COLOR_WINDOW_HEIGHT + 30,
                        30,
                        30,
                        WHITE,
                        "Standard",
                        BLACK,
                        name= "Palbutton",
                        shape= ""
                    ))
        if(len(self.AllPal.palettes)>0 and self.count<8):
            j=0
            for palette in self.AllPal.palettes:
                self.palette_window_buttons.append(
                    Button(
                    self.COLOR_WINDOW_WIDTH +10,
                    self.COLOR_WINDOW_HEIGHT + 30 + j,
                    60,
                    30,
                    WHITE,
                    palette.Name,
                    BLACK,
                ))
                for i in range(9):
                    self.palette_window_buttons.append(
                        Button(
                            self.COLOR_WINDOW_WIDTH+10 + 16 * i,
                            self.COLOR_WINDOW_HEIGHT + 50 + j,
                            15,
                            15,
                            palette.palette[i],
                            name= "Pal"+str(i)+str(self.count)
                        )
                    )
                for i in range(9):
                    self.palette_window_buttons.append(
                        Button(
                            self.COLOR_WINDOW_WIDTH+10 + 16 * i,
                            self.COLOR_WINDOW_HEIGHT + 70 + j,
                            15,
                            15,
                            palette.palette[i + 9],
                            name= "Pal"+str(i + 9)+str(self.count)
                        )
                    )
                j+=90
                self.count+=1    

    def draw_palette_window_buttons(self, win, check):
        if(check == False):
            line_color= (0,0,0)
            pygame.draw.line(win, line_color, (self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 120, self.COLOR_WINDOW_HEIGHT+10 * 1), (self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 120, self.COLOR_WINDOW_HEIGHT *3 +180))
            base_font= get_font(15)
            text= "YOUR PALETTES"
            text_surface= base_font.render(text, True, (0 , 0, 0))
            win.blit(text_surface, (self.COLOR_WINDOW_WIDTH + (self.COLOR_WINDOW_HEIGHT / 2) - 15,
            self.COLOR_WINDOW_HEIGHT+10 * 1))

            base_font= get_font(15)
            text= "CREATE NEW PALETTE"
            text_surface= base_font.render(text, True, (0 , 0, 0))
            win.blit(text_surface, (self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 145,
            self.COLOR_WINDOW_HEIGHT+10 * 1))

            base_font= get_font(15)
            text= "Name:"
            text_surface= base_font.render(text, True, (0 , 0, 0))
            win.blit(text_surface, (self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 130,
            self.COLOR_WINDOW_HEIGHT+20 * 2))

            for i in range(16):
                base_font= get_font(15)
                text= "RGB: "
                text_surface= base_font.render(text, True, (0 , 0, 0))
                win.blit(text_surface, (self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 130,
                self.COLOR_WINDOW_HEIGHT+20 * (i+3)))
            
            if(self.isAppend):
                self.palAppend()
                self.isAppend= False
               
            for button in self.palette_window_buttons:
                if(button.name == None):
                    self.palette_window_buttons.remove(button)
                else:
                    print(button.name)
                    button.draw(win)
        else:
            if(len(self.AllPal.palettes)>self.count):
                j=self.count*90
                for palette in self.AllPal.palettes:
                    self.palette_window_buttons.append(
                        Button(
                        self.COLOR_WINDOW_WIDTH +10,
                        self.COLOR_WINDOW_HEIGHT + 30 + j,
                        60,
                        30,
                        WHITE,
                        palette.Name,
                        BLACK,
                    ))
                    for i in range(9):
                        self.palette_window_buttons.append(
                            Button(
                                self.COLOR_WINDOW_WIDTH+10 + 16 * i,
                                self.COLOR_WINDOW_HEIGHT + 50 + j,
                                15,
                                15,
                                palette.palette[i],
                                name= "Pal"+str(i)+str(self.count)
                            )
                        )
                    for i in range(9):
                        self.palette_window_buttons.append(
                            Button(
                                self.COLOR_WINDOW_WIDTH+10 + 16 * i,
                                self.COLOR_WINDOW_HEIGHT + 70 + j,
                                15,
                                15,
                                palette.palette[i + 9],
                                name= "Pal"+str(i + 9)+str(self.count)
                            )
                        )
                    j+=90
            for button in self.palette_window_buttons:
                button.draw(win)

    def getListIndex(self, name):
        count = 0
        for button in self.palette_window_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1
    
    def buttonText(self):
        check= False
        for button in self.palette_window_buttons:
            if button.name.startswith("Color"):
                if(button.text):
                    check = True
                    break
        return check

    def setText(self):
        r1Ind= self.getListIndex("ColorR1")
        g1Ind= self.getListIndex("ColorG1")
        b1Ind= self.getListIndex("ColorB1")
        r2Ind= self.getListIndex("ColorR2")
        g2Ind= self.getListIndex("ColorG2")
        b2Ind= self.getListIndex("ColorB2")
        r3Ind= self.getListIndex("ColorR3")
        g3Ind= self.getListIndex("ColorG3")
        b3Ind= self.getListIndex("ColorB3")
        r4Ind= self.getListIndex("ColorR4")
        g4Ind= self.getListIndex("ColorG4")
        b4Ind= self.getListIndex("ColorB4")
        r5Ind= self.getListIndex("ColorR5")
        g5Ind= self.getListIndex("ColorG5")
        b5Ind= self.getListIndex("ColorB5")
        r6Ind= self.getListIndex("ColorR6")
        g6Ind= self.getListIndex("ColorG6")
        b6Ind= self.getListIndex("ColorB6")
        r7Ind= self.getListIndex("ColorR7")
        g7Ind= self.getListIndex("ColorG7")
        b7Ind= self.getListIndex("ColorB7")
        r8Ind= self.getListIndex("ColorR8")
        g8Ind= self.getListIndex("ColorG8")
        b8Ind= self.getListIndex("ColorB8")
        r9Ind= self.getListIndex("ColorR9")
        g9Ind= self.getListIndex("ColorG9")
        b9Ind= self.getListIndex("ColorB9")
        r10Ind= self.getListIndex("ColorR10")
        g10Ind= self.getListIndex("ColorG10")
        b10Ind= self.getListIndex("ColorB10")
        r11Ind= self.getListIndex("ColorR11")
        g11Ind= self.getListIndex("ColorG11")
        b11Ind= self.getListIndex("ColorB11")
        r12Ind= self.getListIndex("ColorR12")
        g12Ind= self.getListIndex("ColorG12")
        b12Ind= self.getListIndex("ColorB12")
        r13Ind= self.getListIndex("ColorR13")
        g13Ind= self.getListIndex("ColorG13")
        b13Ind= self.getListIndex("ColorB13")
        r14Ind= self.getListIndex("ColorR14")
        g14Ind= self.getListIndex("ColorG14")
        b14Ind= self.getListIndex("ColorB14")
        r15Ind= self.getListIndex("ColorR15")
        g15Ind= self.getListIndex("ColorG15")
        b15Ind= self.getListIndex("ColorB15")
        r16Ind= self.getListIndex("ColorR16")
        g16Ind= self.getListIndex("ColorG16")
        b16Ind= self.getListIndex("ColorB16")
        if (self.buttonText):
            if self.palette_window_buttons[r1Ind].text:
                self.r1 = int(self.palette_window_buttons[r1Ind].text)
            else :
                self.r1 = 0
            if self.palette_window_buttons[r2Ind].text:
                self.r2 = int(self.palette_window_buttons[r2Ind].text)
            else :
                self.r2 = 0
            if self.palette_window_buttons[r3Ind].text:
                self.r3 = int(self.palette_window_buttons[r3Ind].text)
            else :
                self.r3 = 0
            if self.palette_window_buttons[r4Ind].text:
                self.r4 = int(self.palette_window_buttons[r4Ind].text)
            else :
                self.r4 = 0
            if self.palette_window_buttons[r5Ind].text:
                self.r5 = int(self.palette_window_buttons[r5Ind].text)
            else :
                self.r5 = 0
            if self.palette_window_buttons[r6Ind].text:
                self.r6 = int(self.palette_window_buttons[r6Ind].text)
            else :
                self.r6 = 0
            if self.palette_window_buttons[r7Ind].text:
                self.r7 = int(self.palette_window_buttons[r7Ind].text)
            else :
                self.r7 = 0
            if self.palette_window_buttons[r8Ind].text:
                self.r8 = int(self.palette_window_buttons[r8Ind].text)
            else :
                self.r8 = 0
            if self.palette_window_buttons[r9Ind].text:
                self.r9 = int(self.palette_window_buttons[r9Ind].text)
            else :
                self.r9 = 0
            if self.palette_window_buttons[r10Ind].text:
                self.r10 = int(self.palette_window_buttons[r10Ind].text)
            else :
                self.r10 = 0
            if self.palette_window_buttons[r11Ind].text:
                self.r11 = int(self.palette_window_buttons[r11Ind].text)
            else :
                self.r11 = 0
            if self.palette_window_buttons[r12Ind].text:
                self.r12 = int(self.palette_window_buttons[r12Ind].text)
            else :
                self.r12 = 0
            if self.palette_window_buttons[r13Ind].text:
                self.r13 = int(self.palette_window_buttons[r13Ind].text)
            else :
                self.r13 = 0
            if self.palette_window_buttons[r14Ind].text:
                self.r14 = int(self.palette_window_buttons[r14Ind].text)
            else :
                self.r14 = 0
            if self.palette_window_buttons[r15Ind].text:
                self.r15 = int(self.palette_window_buttons[r15Ind].text)
            else :
                self.r15 = 0
            if self.palette_window_buttons[r16Ind].text:
                self.r16 = int(self.palette_window_buttons[r16Ind].text)
            else :
                self.r16 = 0
            if self.palette_window_buttons[g1Ind].text:
                self.g1 = int(self.palette_window_buttons[g1Ind].text)
            else :
                self.g1 = 0
            if self.palette_window_buttons[g2Ind].text:
                self.g2 = int(self.palette_window_buttons[g2Ind].text)
            else :
                self.g2 = 0
            if self.palette_window_buttons[g3Ind].text:
                self.g3 = int(self.palette_window_buttons[g3Ind].text)
            else :
                self.g3 = 0
            if self.palette_window_buttons[g4Ind].text:
                self.g4 = int(self.palette_window_buttons[g4Ind].text)
            else :
                self.g4 = 0
            if self.palette_window_buttons[g5Ind].text:
                self.g5 = int(self.palette_window_buttons[g5Ind].text)
            else :
                self.g5 = 0
            if self.palette_window_buttons[g6Ind].text:
                self.g6 = int(self.palette_window_buttons[g6Ind].text)
            else :
                self.g6 = 0
            if self.palette_window_buttons[g7Ind].text:
                self.g7 = int(self.palette_window_buttons[g7Ind].text)
            else :
                self.g7 = 0
            if self.palette_window_buttons[g8Ind].text:
                self.g8 = int(self.palette_window_buttons[g8Ind].text)
            else :
                self.g8 = 0
            if self.palette_window_buttons[g9Ind].text:
                self.g9 = int(self.palette_window_buttons[g9Ind].text)
            else :
                self.g9 = 0
            if self.palette_window_buttons[g10Ind].text:
                self.g10 = int(self.palette_window_buttons[g10Ind].text)
            else :
                self.g10 = 0
            if self.palette_window_buttons[g11Ind].text:
                self.g11 = int(self.palette_window_buttons[g11Ind].text)
            else :
                self.g11 = 0
            if self.palette_window_buttons[g12Ind].text:
                self.g12 = int(self.palette_window_buttons[g12Ind].text)
            else :
                self.g12 = 0
            if self.palette_window_buttons[g13Ind].text:
                self.g13 = int(self.palette_window_buttons[g13Ind].text)
            else :
                self.g13 = 0
            if self.palette_window_buttons[g14Ind].text:
                self.g14 = int(self.palette_window_buttons[g14Ind].text)
            else :
                self.g14 = 0
            if self.palette_window_buttons[g15Ind].text:
                self.g15 = int(self.palette_window_buttons[g15Ind].text)
            else :
                self.g15 = 0
            if self.palette_window_buttons[g16Ind].text:
                self.g16 = int(self.palette_window_buttons[g16Ind].text)
            else :
                self.g16 = 0
            if self.palette_window_buttons[b1Ind].text:
                self.b1 = int(self.palette_window_buttons[b1Ind].text)
            else :
                self.b1 = 0
            if self.palette_window_buttons[b2Ind].text:
                self.b2 = int(self.palette_window_buttons[b2Ind].text)
            else :
                self.b2 = 0
            if self.palette_window_buttons[b3Ind].text:
                self.b3 = int(self.palette_window_buttons[b3Ind].text)
            else :
                self.b3 = 0
            if self.palette_window_buttons[b4Ind].text:
                self.b4 = int(self.palette_window_buttons[b4Ind].text)
            else :
                self.b4 = 0
            if self.palette_window_buttons[b5Ind].text:
                self.b5 = int(self.palette_window_buttons[b5Ind].text)
            else :
                self.b5 = 0
            if self.palette_window_buttons[b6Ind].text:
                self.b6 = int(self.palette_window_buttons[b6Ind].text)
            else :
                self.b6 = 0
            if self.palette_window_buttons[b7Ind].text:
                self.b7 = int(self.palette_window_buttons[b7Ind].text)
            else :
                self.b7 = 0
            if self.palette_window_buttons[b8Ind].text:
                self.b8 = int(self.palette_window_buttons[b8Ind].text)
            else :
                self.b8 = 0
            if self.palette_window_buttons[b9Ind].text:
                self.b9 = int(self.palette_window_buttons[b9Ind].text)
            else :
                self.b9 = 0
            if self.palette_window_buttons[b10Ind].text:
                self.b10 = int(self.palette_window_buttons[b10Ind].text)
            else :
                self.b10 = 0
            if self.palette_window_buttons[b11Ind].text:
                self.b11 = int(self.palette_window_buttons[b11Ind].text)
            else :
                self.b11 = 0
            if self.palette_window_buttons[b12Ind].text:
                self.b12 = int(self.palette_window_buttons[b12Ind].text)
            else :
                self.b12 = 0
            if self.palette_window_buttons[b13Ind].text:
                self.b13 = int(self.palette_window_buttons[b13Ind].text)
            else :
                self.b13 = 0
            if self.palette_window_buttons[b14Ind].text:
                self.b14 = int(self.palette_window_buttons[b14Ind].text)
            else :
                self.b14 = 0
            if self.palette_window_buttons[b15Ind].text:
                self.b15 = int(self.palette_window_buttons[b15Ind].text)
            else :
                self.b15 = 0
            if self.palette_window_buttons[b16Ind].text:
                self.b16 = int(self.palette_window_buttons[b16Ind].text)
            else :
                self.b1
        

    

