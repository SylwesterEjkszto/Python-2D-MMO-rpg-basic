from tkinter import *
from PIL import Image
class Player():
    def __init__(self):
        self.name = ""
        self.hp = 1
        self.xp = 1
        self.clan = ""
        self.map = 'assets/testmap.png'
        self.x_coordinate = 0
        self.y_coordinate = 1
        self.asset = 'assets/player.png'