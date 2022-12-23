from turtle import pos
from .settings import *
from .Palette import *

class AllPalettes:
    def __init__(self):
        self.palettes= []

    def store(self, newPalette):
        pal= Palette()
        pal.palette= list(newPalette.palette)
        pal.Name= newPalette.Name
        self.palettes.append(pal)
    
    def getPalIndex(self, name):
        count=0
        for palette in self.palettes:
            if(palette.Name == name):
                return count
            count= count+1
        return -1

    def checkName(self, nm):
        check= False
        for palette in self.palettes:
            if palette.Name == nm:
                check =True
                break

        return check

    def delete(self, name):
        for palette in self.palettes:
            if(palette.getName()==name):
                self.palettes.remove(palette)
        