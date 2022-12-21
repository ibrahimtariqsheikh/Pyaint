from turtle import pos
from .settings import *

class Palette:
    palette= []
    Name= None

    def setColor(self, color):
        self.palette.append(color)

    def setName(self, name):
        self.Name= name

    def getRGBstatus(colormode):
        if(colormode==True):
            return True
        else :
            return False
        
    def getName(self):
        return self.Name
        
    #def convertHSVtoRGB(colorHSV):

