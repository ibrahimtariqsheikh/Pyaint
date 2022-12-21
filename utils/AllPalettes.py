from turtle import pos
from .settings import *

class AllPalettes:
    def __init__(self):
        self.palettes= []

    def store(self, newPalette):
        if(len(self.palettes)<8):
            self.palettes.append(newPalette)
    
    def delete(self, name):
        for palette in self.palettes:
            if(palette.getName()==name):
                self.palettes.remove(palette)
        