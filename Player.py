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
        self.map = 1
        self.x = 465
        self.y = 385
        self.asset = 'assets/standing.png'
        # 1 - left 2 -right 3 - down 4- up
        self.last_used_movement_direction = 0
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.active = "active"
        self.walkRight = [('assets/R1.png'),('assets/R2.png'),('assets/R3.png'),
                     ('assets/R4.png'),('assets/R5.png'), ('assets/R6.png'),
                     ('assets/R7.png'),('assets/R8.png'), ('assets/R9.png')]
        self.walkLeft = [('assets/L1.png'), ('assets/L2.png'), ('assets/L3.png'),
                    ('assets/L4.png'), ('assets/L5.png'), ('assets/L6.png'),
                    ('assets/L7.png'), ('assets/L8.png'), ('assets/L9.png')]
        self.walkDown = [("assets/standing.png"),("assets/D2.png"),("assets/D3.png")]
        self.walkUp = [("assets/up1.png"), ("assets/up2.png"),("assets/up3.png")]
        self.walk_count = 0
        self.collision_rect = 0
    def update(self, speed):
        self.walk_count += speed
        if self.last_used_movement_direction == 1 and int(self.walk_count) >= len(self.walkLeft):
            self.walk_count = 0
        if self.last_used_movement_direction == 2 and int(self.walk_count) >= len(self.walkRight):
            self.walk_count = 0
        if self.last_used_movement_direction == 3 and int(self.walk_count) >= len(self.walkDown):
            self.walk_count = 0
        if self.last_used_movement_direction == 4 and int(self.walk_count) >= len(self.walkUp):
            self.walk_count = 0
    def update_hitbox(self,camera_x,camera_y):
        self.hitbox = (self.x + 17 - camera_x, self.y + 11 - camera_y, 29, 52)
        self.collision_rect = pygame.Rect(self.hitbox)