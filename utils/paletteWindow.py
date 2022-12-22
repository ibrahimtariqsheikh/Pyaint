from .settings import *
from .button import *
from .AllPalettes import *
from .Palette import *

class PaletteWindow:
    def __init__(self):
        self.currentPalette= 0
        self.count=0
        self.j=0
        self.isAppend= True
        self.AllPal= AllPalettes()
        self.isPaletteWindow = False
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
        self.r17 = 0
        self.g17 = 0
        self.b17 = 0
        self.r18 = 0
        self.g18 = 0
        self.b18 = 0
        self.name= ""
        self.rect_x_y = [370,162,413,162,456,162,370,182,413,182,456,182,370,202,413,202,456,202,370,222,413,222,456,222,370,242,413,242,456,242,370,262,413,262,456,262,370,282,413,282,456,282,370,302,413,302,456,302,370,322,413,322,456,322,370,342,413,342,456,342,370,362,413,362,456,362,370,382,413,382,456,382,370,402,413,402,456,402,370,422,413,422,456,
                        422,370,442,413,442,456,442,370,462,413,462,456,462,370,482,413,482,456,482,370,502,413,502,456,502,]
        self.COLOR_WINDOW_SIZE = 400
        self.COLOR_WINDOW_WIDTH = WIDTH / 2 - self.COLOR_WINDOW_SIZE / 2
        self.COLOR_WINDOW_HEIGHT = WIDTH / 2 - self.COLOR_WINDOW_SIZE / 2 
        self.palette_window_buttons = [
            Button(
                self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_SIZE - 25 - 5+50,
                self.COLOR_WINDOW_HEIGHT + 5,
                25,
                25,
                color=WHITE,
                name="ClosePaletteWindow",
                image_url="assets/close_color_window.png",
            ),
            Button(
                self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 130 + 40+50,
                self.COLOR_WINDOW_HEIGHT+20 * 2,
                80,
                15,
                WHITE,
                name="PaletteName",
            ),
            Button(
                self.COLOR_WINDOW_WIDTH + self.COLOR_WINDOW_HEIGHT / 2 + 130 + 170+10,
                self.COLOR_WINDOW_HEIGHT+425,
                40,
                15,
                WHITE,
                name="SavePalette",
                text="Save",
                shape="",
            ),
            Button(
                self.COLOR_WINDOW_WIDTH +10+5+50,
                self.COLOR_WINDOW_HEIGHT + self.j+35,
                15,
                15,
                WHITE,
                name="TickPalette",
                image_url="assets/tick.png",
                shape="",
            ),
            Button(
                self.COLOR_WINDOW_WIDTH+50 + self.COLOR_WINDOW_HEIGHT / 2 + 130+70,
                self.COLOR_WINDOW_HEIGHT+20 * 2+420,
                40,
                15,
                WHITE,
                name="Error Message",
                text="",
                shape="",
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
            ),
            Button(
                int(self.rect_x_y[96]),
                int(self.rect_x_y[97]),
                40,
                15,
                WHITE,
                name="ColorR17",
            ),
            Button(
                int(self.rect_x_y[98]),
                int(self.rect_x_y[99]),
                40,
                15,
                WHITE,
                name="ColorG17",
            ),
            Button(
                int(self.rect_x_y[100]),
                int(self.rect_x_y[101]),
                40,
                15,
                WHITE,
                name="ColorB17",
            ),
            Button(
                int(self.rect_x_y[102]),
                int(self.rect_x_y[103]),
                40,
                15,
                WHITE,
                name="ColorR18",
            ),
            Button(
                int(self.rect_x_y[104]),
                int(self.rect_x_y[105]),
                40,
                15,
                WHITE,
                name="ColorG18",
            ),
            Button(
                int(self.rect_x_y[106]),
                int(self.rect_x_y[107]),
                40,
                15,
                WHITE,
                name="ColorB18",
            )
        ]

    def draw_palette_window(self, win):
        pygame.draw.rect(
            win,
            (255, 255, 255),
            (
                self.COLOR_WINDOW_WIDTH,
                self.COLOR_WINDOW_HEIGHT,
                self.COLOR_WINDOW_SIZE+50,
                self.COLOR_WINDOW_SIZE+150,
            ),
            width=0,
        )
        pygame.draw.rect(
            win,
            (0, 0, 0),
            (
                self.COLOR_WINDOW_WIDTH,
                self.COLOR_WINDOW_HEIGHT,
                self.COLOR_WINDOW_SIZE+50,
                self.COLOR_WINDOW_SIZE+150,
            ),
            width=2,
        )

    def deletePalette(self, button):
        self.palette_window_buttons[self.getListIndex("Error Message")].text=""
        ind= self.getListIndex("Palbutton"+str(button.name[6]))
        delname="Palbutton"
        sc=0
        delname+=button.name[6]
        sc= int(button.name[6])
        sc1= int(button.name[6])
        
        if(self.AllPal.getPalIndex(self.palette_window_buttons[self.getListIndex(delname)].text)==self.currentPalette):
            self.selectPalette(self.palette_window_buttons[self.getListIndex("Palbutton1")])

        self.AllPal.delete(self.palette_window_buttons[ind].text)
        

        for btn in self.palette_window_buttons:
            if btn.name == delname:
                self.palette_window_buttons.remove(btn)
        while(self.getListIndex("Pal"+str(sc))!=-1):
            del self.palette_window_buttons[self.getListIndex("Pal"+str(sc))]
        
        del self.palette_window_buttons[self.getListIndex(button.name)]
        self.count=self.count-1

        sc1+=1
        while(self.getListIndex("Palbutton"+str(sc1))!=-1 and sc1<9):
            ind= self.getListIndex("Palbutton"+str(sc1))
            self.palette_window_buttons[ind].y= self.palette_window_buttons[ind].y-55
            self.palette_window_buttons[ind].name= "Palbutton"+str(sc1-1)
            sc1+=1
        
        sc+=1
        while(self.getListIndex("Pal"+str(sc))!=-1 and sc<9):
            while(self.getListIndex("Pal"+str(sc))!=-1):
                ind= self.getListIndex("Pal"+str(sc))
                self.palette_window_buttons[ind].y= self.palette_window_buttons[ind].y-55
                self.palette_window_buttons[ind].name= "Pal"+str(sc-1)
            sc+=1
        
        sc1= int(button.name[6])
        sc1+=1
        while(self.getListIndex("Delete"+str(sc1))!=-1 and sc1<9):
            ind= self.getListIndex("Delete"+str(sc1))
            self.palette_window_buttons[ind].y= self.palette_window_buttons[ind].y-55
            self.palette_window_buttons[ind].name= "Delete"+str(sc1-1)
            sc1+=1

        self.j=self.j-55
        


        
            
        

    def palAppend(self, palette, name):
        if(self.count<8):
            self.count+=1
            if(self.isAppend==True):
                self.AllPal.store(palette)
                self.name=name
                self.j+=30
            else:
                self.j+=10

            self.palette_window_buttons.append(
                Button(
                self.COLOR_WINDOW_WIDTH +10+5,
                self.COLOR_WINDOW_HEIGHT + self.j,
                40,
                30,
                WHITE,
                self.name,
                BLACK,
                name= "Palbutton"+str(self.count),
                shape= ""
            ))
            if(self.isAppend==False):
                self.palette_window_buttons.append(
                    Button(
                        self.COLOR_WINDOW_WIDTH +170,
                        self.COLOR_WINDOW_HEIGHT + self.j+30,
                        25,
                        25,
                        color=WHITE,
                        name="Delete"+str(self.count),
                        image_url="assets/trash-bin.png",
                    ))
            self.j+=25
            for i in range(9):
                self.palette_window_buttons.append(
                    Button(
                        self.COLOR_WINDOW_WIDTH+10 + 16 * i,
                        self.COLOR_WINDOW_HEIGHT + self.j,
                        15,
                        15,
                        palette.palette[i],
                        name= "Pal"+str(self.count)
                    )
                )
            self.j+=20
            for i in range(9):
                self.palette_window_buttons.append(
                    Button(
                        self.COLOR_WINDOW_WIDTH+10 + 16 * i,
                        self.COLOR_WINDOW_HEIGHT + self.j,
                        15,
                        15,
                        palette.palette[i + 9],
                        name= "Pal"+str(self.count)
                    )
                )
            self.isAppend= False   

    def selectPalette(self, button):
        chng= self.AllPal.getPalIndex(button.text)
        if(self.currentPalette!=int(chng)):
            self.currentPalette= chng
            tickInd= self.getListIndex("TickPalette")
            self.palette_window_buttons[tickInd].y= int(button.y+5)

    def draw_palette_window_buttons(self, win, check):
        if(check == False):
            line_color= (0,0,0)
            pygame.draw.line(win, line_color, (self.COLOR_WINDOW_WIDTH+50 + self.COLOR_WINDOW_HEIGHT / 2 + 120, self.COLOR_WINDOW_HEIGHT+10 * 1), (self.COLOR_WINDOW_WIDTH+50 + self.COLOR_WINDOW_HEIGHT / 2 + 120, self.COLOR_WINDOW_HEIGHT *3 +180+150))
            base_font= get_font(15)
            text= "YOUR PALETTES"
            text_surface= base_font.render(text, True, (0 , 0, 0))
            win.blit(text_surface, (self.COLOR_WINDOW_WIDTH + (self.COLOR_WINDOW_HEIGHT / 2) - 15+20,
            self.COLOR_WINDOW_HEIGHT+10 * 1))

            base_font= get_font(15)
            text= "CREATE NEW PALETTE"
            text_surface= base_font.render(text, True, (0 , 0, 0))
            win.blit(text_surface, (self.COLOR_WINDOW_WIDTH+50 + self.COLOR_WINDOW_HEIGHT / 2 + 145+10,
            self.COLOR_WINDOW_HEIGHT+10 * 1))

            base_font= get_font(15)
            text= "Name:"
            text_surface= base_font.render(text, True, (0 , 0, 0))
            win.blit(text_surface, (self.COLOR_WINDOW_WIDTH+50 + self.COLOR_WINDOW_HEIGHT / 2 + 130,
            self.COLOR_WINDOW_HEIGHT+20 * 2))

            base_font= get_font(15)
            text= "Error:"
            text_surface= base_font.render(text, True, (0 , 0, 0))
            win.blit(text_surface, (self.COLOR_WINDOW_WIDTH+50 + self.COLOR_WINDOW_HEIGHT / 2 + 130,
            self.COLOR_WINDOW_HEIGHT+20 * 2+400))


            for i in range(18):
                base_font= get_font(15)
                text= "RGB: "
                text_surface= base_font.render(text, True, (0 , 0, 0))
                win.blit(text_surface, (self.COLOR_WINDOW_WIDTH+50 + self.COLOR_WINDOW_HEIGHT / 2 + 130,
                self.COLOR_WINDOW_HEIGHT+20 * (i+3)))
               
            for button in self.palette_window_buttons:
                button.draw(win)
        else:
            for button in self.palette_window_buttons:
                button.draw(win)

    def getListIndex(self, name):
        count = 0
        for button in self.palette_window_buttons:
            if button.name == name:
                return count
            count = count + 1
        return -1

    def savePalette(self):
        if(len(self.AllPal.palettes)<8):
            pal= Palette()
            RGB1= (self.r1, self.g1, self.b1)
            RGB2= (self.r2, self.g2, self.b2)
            RGB3= (self.r3, self.g3, self.b3)
            RGB4= (self.r4, self.g4, self.b4)
            RGB5= (self.r5, self.g5, self.b5)
            RGB6= (self.r6, self.g6, self.b6)
            RGB7= (self.r7, self.g7, self.b7)
            RGB8= (self.r8, self.g8, self.b8)
            RGB9= (self.r9, self.g9, self.b9)
            RGB10= (self.r10, self.g10, self.b10)
            RGB11= (self.r11, self.g11, self.b11)
            RGB12= (self.r12, self.g12, self.b12)
            RGB13= (self.r13, self.g13, self.b13)
            RGB14= (self.r14, self.g14, self.b14)
            RGB15= (self.r15, self.g15, self.b15)
            RGB16= (self.r16, self.g16, self.b16)
            RGB17= (self.r17, self.g17, self.b17)
            RGB18= (self.r18, self.g18, self.b18)
            pal.palette[0]=RGB1
            pal.palette[1]=RGB2
            pal.palette[2]=RGB3
            pal.palette[3]=RGB4
            pal.palette[4]=RGB5
            pal.palette[5]=RGB6
            pal.palette[6]=RGB7
            pal.palette[7]=RGB8
            pal.palette[8]=RGB9
            pal.palette[9]=RGB10
            pal.palette[10]=RGB11
            pal.palette[11]=RGB12
            pal.palette[12]=RGB13
            pal.palette[13]=RGB14
            pal.palette[14]=RGB15
            pal.palette[15]=RGB16
            pal.palette[16]=RGB17
            pal.palette[17]=RGB18

            self.setPaletteName()
            pal.Name= self.name
            if(self.AllPal.checkName(self.name)==False):
                self.palAppend(pal, self.name)
                self.AllPal.store(pal)
                self.palette_window_buttons[self.getListIndex("Error Message")].text=""
            else:
                self.palette_window_buttons[self.getListIndex("Error Message")].text="Please enter palette name!"
        else:
            self.palette_window_buttons[self.getListIndex("Error Message")].text="No more palettes can be created."

    
    def buttonText(self):
        check= False
        for button in self.palette_window_buttons:
            if button.name.startswith("Color"):
                if(button.text):
                    check = True
                    break
        return check

    def setPaletteName(self):
        PNameIND= self.getListIndex("PaletteName")
        if(self.palette_window_buttons[PNameIND].text):
            self.name= self.palette_window_buttons[PNameIND].text
        else:
            self.name= "Palette"+str(self.count)

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
        r17Ind= self.getListIndex("ColorR17")
        g17Ind= self.getListIndex("ColorG17")
        b17Ind= self.getListIndex("ColorB17")
        r18Ind= self.getListIndex("ColorR18")
        g18Ind= self.getListIndex("ColorG18")
        b18Ind= self.getListIndex("ColorB18")
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

            if self.palette_window_buttons[r17Ind].text:
                self.r17 = int(self.palette_window_buttons[r17Ind].text)
            else :
                self.r17 = 0
            
            if self.palette_window_buttons[r18Ind].text:
                self.r18 = int(self.palette_window_buttons[r18Ind].text)
            else :
                self.r18 = 0
            
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

            if self.palette_window_buttons[g17Ind].text:
                self.g17 = int(self.palette_window_buttons[g17Ind].text)
            else :
                self.g17 = 0
            
            if self.palette_window_buttons[g18Ind].text:
                self.g18 = int(self.palette_window_buttons[g18Ind].text)
            else :
                self.g18 = 0
            
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
                self.b16 = 0

            if self.palette_window_buttons[b17Ind].text:
                self.b17 = int(self.palette_window_buttons[b17Ind].text)
            else :
                self.b17 = 0
            
            if self.palette_window_buttons[b18Ind].text:
                self.b18 = int(self.palette_window_buttons[b18Ind].text)
            else :
                self.b18 = 0
        

    

