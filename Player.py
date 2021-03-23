from tkinter import *
from PIL import Image
class Player():
    def __init__(self):
        self.name = ""
        self.hp = 1
        self.xp = 1
        self.clan = ""
        self.map = 'assets/testmap.png'
        self.x_coordinate = 5
        self.y_coordinate = 5
        self.asset = 'assets/standing.png'