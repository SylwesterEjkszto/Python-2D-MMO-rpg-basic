from tkinter import *
from PIL import Image
import pygame
class Player():
    def __init__(self):
        self.name = ""
        self.hp = 50
        self.max_hp = 50
        self.energy = 10
        self.max_energy = 10
        self.xp = 1
        self.next_lvl = 10
        self.lvl = 1
        self.ability_to_learn = 1
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


