from gamehandler import *
import math
import pygame

class enemy():
    def __init__(self, xpos, ypos, life, speed, sprite, height, width):
        self.enemy_x = xpos
        self.enemy_y = ypos
        self.enemy_life = life
        self.enemy_speed = speed
        self.enemy_is_alive = True
        self.enemy_image = sprite
        self.enemy_rect = pygame.Rect(self.enemy_x, self.enemy_y, height, width)
        self.enemy_diagonal_movement = False
        self.enemy_x_moving = False
        self.enemy_y_moving = False
        self.enemy_damage = 1
        self.colision_location = {
            "left" : False,
            "right" : False,
            "top" : False,
            "bottom" : False
        }

    def move_x(self, dir):
        if self.enemy_x_moving and self.enemy_y_moving:
            self.enemy_speed_diagonal = self.enemy_speed / math.sqrt(math.pow(self.enemy_speed, 2) + math.pow(self.enemy_speed, 2)) * self.enemy_speed
            self.enemy_x = self.enemy_x + dir * self.enemy_speed_diagonal
        else:
            self.enemy_x = self.enemy_x + dir * self.enemy_speed
        self.update_rect()

    def move_y(self, dir):
        if self.enemy_x_moving and self.enemy_y_moving:
            self.enemy_speed_diagonal = self.enemy_speed / math.sqrt(
                math.pow(self.enemy_speed, 2) + math.pow(self.enemy_speed, 2)) * self.enemy_speed
            self.enemy_y = self.enemy_y + dir * self.enemy_speed_diagonal
        else:
            self.enemy_y = self.enemy_y + dir * self.enemy_speed
        self.update_rect()

    def lose_life(self, damage):
        self.enemy_life -= damage

    def gain_life(self, heal):
        self.enemy_life += heal

    def die(self):
        if self.enemy_life <= 0:
            self.enemy_is_alive = False

    def load_sprite(self):
        img = pygame.image.load(self.enemy_image)
        new_img = pygame.transform.scale(img, (self.enemy_rect.height, self.enemy_rect.width))
        return new_img

    def update_rect(self):
        self.enemy_rect.x = self.enemy_x
        self.enemy_rect.y = self.enemy_y
    def return_tuple_pos(self):
        return (self.enemy_x, self.enemy_y)

    def detect_colision(self, entite):
        if entite.x + entite.width > self.enemy_x + self.enemy_rect.width/2 and entite.x - entite.width < self.enemy_x - self.enemy_rect.width/2:
            if entite.y + entite.height > self.enemy_y + self.enemy_rect.height/4 and entite.y - entite.height < self.enemy_y - self.enemy_rect.height/4:
                if entite.x > self.enemy_x:
                    self.colision_location["right"] = True
                if entite.x < self.enemy_x:
                    self.colision_location["left"] = True
                if entite.y > self.enemy_y:
                    self.colision_location["bottom"] = True
                if entite.y < self.enemy_y:
                    self.colision_location["top"] = True
    def detect_colision_with(self, entite):
        if entite.x + entite.width > self.enemy_x + self.enemy_rect.width / 2 and entite.x - entite.width < self.enemy_x - self.enemy_rect.width / 2:
            if entite.y + entite.height > self.enemy_y + self.enemy_rect.height / 4 and entite.y - entite.height < self.enemy_y - self.enemy_rect.height / 4:
                return True


    def clean_colisions(self):
        self.colision_location["right"] = False
        self.colision_location["left"] = False
        self.colision_location["bottom"] = False
        self.colision_location["top"] = False
    def enemy_movement(self, player):

        if player.player_x > self.enemy_x and not self.colision_location["right"]:
            self.move_x(1)
            self.enemy_x_moving = True


        else:
            self.enemy_x_moving = False

        if player.player_x < self.enemy_x and not self.colision_location["left"]:
            self.move_x(-1)
            self.enemy_x_moving = True

        else:
            self.enemy_x_moving = False


        if player.player_y > self.enemy_y and not self.colision_location["bottom"]:
            self.move_y(1)
            self.enemy_y_moving = True

        else:
            self.enemy_y_moving = False

        if player.player_y < self.enemy_y and not self.colision_location["top"]:
            self.move_y(-1)
            self.enemy_y_moving = True

        else:
            self.enemy_y_moving = False