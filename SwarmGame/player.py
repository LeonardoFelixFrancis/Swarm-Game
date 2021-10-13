import math
import pygame
from gamehandler import *

class player():
    def __init__(self, xpos, ypos, life, speed, sprite, height, width):
        self.player_x = xpos
        self.player_y = ypos
        self.player_life = life
        self.player_speed = speed
        self.is_alive = True
        self.player_image = sprite
        self.player_rect = pygame.Rect(self.player_x, self.player_y, height, width)
        self.diagonal_movement = False
        self.score = 0
    def move_x(self, dir):
        if self.diagonal_movement:
            self.player_speed_diagonal = self.player_speed/math.sqrt(math.pow(self.player_speed,2) + math.pow(self.player_speed,2)) * self.player_speed
            self.player_x = self.player_x + dir * self.player_speed_diagonal
        else:
            self.player_x = self.player_x + dir * self.player_speed
        self.update_rect()
    def move_y(self, dir):
        if self.diagonal_movement:
            self.player_speed_diagonal = self.player_speed/math.sqrt(math.pow(self.player_speed,2) + math.pow(self.player_speed,2)) * self.player_speed
            self.player_y = self.player_y + dir * self.player_speed_diagonal
        else:
            self.player_y = self.player_y + dir * self.player_speed
        self.update_rect()

    def lose_life(self, damage):
        self.player_life -= damage
    def gain_life(self, heal):
        self.player_life += heal
    def die(self):
        if self.player_life <= 0:
            self.is_alive = False
    def load_sprite(self):
        img = pygame.image.load(self.player_image)
        new_img = pygame.transform.scale(img, (self.player_rect.height, self.player_rect.width))
        return new_img
    def update_rect(self):
        self.player_rect.x = self.player_x
        self.player_rect.y = self.player_y
    def return_tuple_pos(self):
        return (self.player_x, self.player_y)

    def get_dir_to_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        delta_x = mouse_pos[0] - self.player_x

        delta_y = mouse_pos[1] - self.player_y

        normalized_delta_x = 0
        normalized_delta_y = 0
        if delta_x != 0:
            normalized_delta_x = delta_x/math.sqrt((math.pow(delta_x,2) + math.pow(delta_y,2)))
        if delta_y != 0:
            normalized_delta_y = delta_y/math.sqrt((math.pow(delta_x, 2) + math.pow(delta_y, 2)))

        return (normalized_delta_x, normalized_delta_y)

class bullet():
    def __init__(self, posx, posy, speed, image, height, width, dir):
        self.posx = posx
        self.posy = posy
        self.speed = speed
        self.img = image
        self.height = height
        self.width = width
        self.dir = dir
        self.bullet_rect = pygame.Rect(self.posx, self.posy, height, width)
        self.colided = False
    def move(self):
        self.posx += self.speed * self.dir[0]
        self.posy += self.speed * self.dir[1]
        self.update_rect()
    def update_rect(self):
        self.bullet_rect.x = self.posx
        self.bullet_rect.y = self.posy
    def load_sprite(self):
        img = pygame.image.load(self.img)
        new_img = pygame.transform.scale(img, (self.bullet_rect.height, self.bullet_rect.width))
        return new_img
    def return_tuple_pos(self):
        return (self.posx, self.posy)

    def detect_colision_with(self, entite):
        if entite.x + entite.width > self.posx + self.bullet_rect.width / 2 and entite.x - entite.width < self.posx - self.bullet_rect.width / 2:
            if entite.y + entite.height > self.posy + self.bullet_rect.height / 4 and entite.y - entite.height < self.posy - self.bullet_rect.height / 4:
                return True