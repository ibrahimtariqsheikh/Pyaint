from .settings import *
from .button import *
from .AllPalettes import *
from .Palette import *
import copy


class Grayscale:
    def __init__(self):
        self.palette= Palette()
    
    def setUp(self, palette):
        for i in range(18):
            self.palette.palette[i]= copy.copy(palette.palette[i])

