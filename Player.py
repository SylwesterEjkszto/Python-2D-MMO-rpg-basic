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
        self.x = 465
        self.y = 385
        self.asset = 'assets/standing.png'
        self.left = 0
        self.right = 0
        self.down = 0
        self.up = 0
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.active = "active"


