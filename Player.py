from tkinter import *
from PIL import Image
import pygame
class Player():
    def __init__(self):
        self.name = ""
        self.hp = 1
        self.xp = 1
        self.clan = ""
        self.map = 'assets/pierwszamapa.png'
        self.x_coordinate = 465
        self.y_coordinate = 385
        self.asset = 'assets/standing.png'
        self.left = 0
        self.right = 0
        self.down = 0
        self.up = 0
        self.hitbox = (self.x_coordinate + 17, self.y_coordinate + 11, 29, 52)
        self.active = "active"


