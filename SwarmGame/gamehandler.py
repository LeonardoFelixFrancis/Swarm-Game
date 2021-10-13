import pygame
from player import *
from enemy import *
import random

class game_handler:
    def __init__(self, screen_name, height, width):
        pygame.init()
        self.screen = pygame.display.set_mode((height, width))
        pygame.display.set_caption(screen_name)
        self.game_is_runing = True
        self.bullets = []
        self.gui_life_pos_x = 20
        self.gui_life_pos_y = 20
        self.heart_img = "assets/heart.png"
        self.heart_rect = pygame.Rect(self.gui_life_pos_x, self.gui_life_pos_y, 32,32)
        self.game_is_on = False
    def event_handle(self, player_obj):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_is_runing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_is_on:
                    self.bullets.append(self.create_bullet(player_obj, player_obj.get_dir_to_mouse(), 5))
                if self.screen.get_width()/2 > pygame.mouse.get_pos()[0] and self.screen.get_width()/2 - 64 < pygame.mouse.get_pos()[0] and not self.game_is_on:
                    if self.screen.get_height() / 2 + 32 > pygame.mouse.get_pos()[1] and self.screen.get_height() / 2 - 32 < pygame.mouse.get_pos()[1]:
                        self.game_is_on = True
                        player_obj.is_alive = True
                        player_obj.player_life = 5

                if self.screen.get_width()/2 > pygame.mouse.get_pos()[0] and self.screen.get_width()/2 - 64 < pygame.mouse.get_pos()[0] and not self.game_is_on:
                    if self.screen.get_height() / 2 + 104 > pygame.mouse.get_pos()[1] and self.screen.get_height() / 2 + 40 < pygame.mouse.get_pos()[1]:
                        self.game_is_runing = False
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[pygame.K_s] and keys_pressed[pygame.K_d]) or (keys_pressed[pygame.K_s] and keys_pressed[pygame.K_a]) or (keys_pressed[pygame.K_w] and keys_pressed[pygame.K_d])  or (keys_pressed[pygame.K_w] and keys_pressed[pygame.K_a]):
            player_obj.diagonal_movement = True
        else:
            player_obj.diagonal_movement = False

        if keys_pressed[pygame.K_d] and player_obj.player_x < self.screen.get_width() - player_obj.player_rect.width:
            player_obj.move_x(1)
        if keys_pressed[pygame.K_a] and player_obj.player_x > 0:
            player_obj.move_x(-1)
        if keys_pressed[pygame.K_w] and player_obj.player_y > 0:
            player_obj.move_y(-1)
        if keys_pressed[pygame.K_s] and player_obj.player_y < self.screen.get_height() - player_obj.player_rect.height:
            player_obj.move_y(1)



    def render_obj(self, obj):
        self.screen.blit(obj.load_sprite(), obj.return_tuple_pos())
    def background_fill(self,color):
        self.screen.fill(color)
    def render(self):
        pygame.display.update()
    def create_enemy(self):
        return enemy(random.randrange(0, self.screen.get_width() - 32),random.randrange(0, self.screen.get_height() - 32), 1, random.randrange(1,3), "assets/enemy.png", 32,32)
    def create_player(self):
        return player(0,0, 5, 3, "assets/player.png", 32, 32)
    def create_bullet(self, player, dir, speed):
        return bullet(player.player_x + 5,player.player_y, speed, "assets/bullet.png", 10, 10, dir)
    def draw_heart_gui(self, player):
        img = pygame.image.load(self.heart_img)
        new_img = pygame.transform.scale(img, (self.heart_rect.height, self.heart_rect.width))
        for i in range(player.player_life):
            self.screen.blit(new_img, (self.heart_rect.x + (32 * i ), self.heart_rect.y))
    def draw_gui(self, img, posx, posy, height, width):
        gui_rect = pygame.Rect(posx, posy, height, width)
        gui_img = pygame.image.load(img)
        gui_img_resize = pygame.transform.scale(gui_img, (height, width))
        self.screen.blit(gui_img_resize, (gui_rect.x, gui_rect.y))