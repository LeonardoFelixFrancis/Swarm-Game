import random
import pygame
from gamehandler import *
from player import *
from enemy import *

FPS = 60
game = game_handler("Swarm", 1200, 800)
player_01 = game.create_player()
enemys = []
time = 0
dificult = 99
dificult_change = 0.05

def main_renderer():

    if(not game.game_is_on):

        game.draw_gui("assets/play.png", (game.screen.get_width() / 2) - 64, (game.screen.get_height() / 2) - 32, 64, 64)
        game.draw_gui("assets/logout.png", (game.screen.get_width() / 2) - 64, (game.screen.get_height() / 2) + 40, 64, 64)

    if(game.game_is_on):
        game.render_obj(player_01)
        game.draw_heart_gui(player_01)
        for enn in enemys:
            game.render_obj(enn)
        for b in game.bullets:
            game.render_obj(b)

def update():
    if(game.game_is_on):
        for enn in enemys:

            for other in enemys:
                if enn != other:
                    enn.detect_colision(other.enemy_rect)
            enn.detect_colision(player_01.player_rect)
            if(enn.detect_colision_with(player_01.player_rect)):
                global time
                if time >= 20:
                    player_01.lose_life(enn.enemy_damage)
                    time = 0
                time += 1
            enn.enemy_movement(player_01)
            enn.clean_colisions()

            if enn.enemy_life <= 0:
                enemys.remove(enn)
                player_01.score += 1
        global dificult
        if random.randrange(0, 100) >= dificult and len(enemys) < 150:
            enemys.append(game.create_enemy())
            if dificult >= 93:
                dificult = dificult - dificult_change

        for b in game.bullets:
            for enn in enemys:
                if b.detect_colision_with(enn.enemy_rect):
                    enn.lose_life(enn.enemy_damage)
                    b.colided = True
                if b.posx < 0 or b.posx > game.screen.get_width() or b.posy < 0 or b.posy > game.screen.get_height():
                    b.colided = True
            b.move()
            if b.colided:
                game.bullets.remove(b)

        player_01.die()
        if not player_01.is_alive:
            game.game_is_on = False



def main():
    clock = pygame.time.Clock()
    while game.game_is_runing:
        clock.tick(FPS)
        game.background_fill((0,250,0))
        main_renderer()
        game.event_handle(player_01)
        update()
        game.render()

        if not game.game_is_on:
            enemys.clear()
            player_01.player_x = random.randrange(0, game.screen.get_width())
            player_01.player_y = random.randrange(0, game.screen.get_height())
            dificult = 99


#PROGRAM
if __name__ == "__main__":
    main()