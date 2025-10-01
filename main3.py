import pygame as pg
import random as rd
import time as t

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)
COLOR = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

x, y = WIDTH / 2, HEIGHT / 2
r = 30
pg.draw.circle(screen, ORANGE, (x, y), r)
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    keys = pg.key.get_pressed()
    if keys[pg.K_a] and x != 30:
        x -= 3
    if keys[pg.K_d] and x + 30 != WIDTH:
        x += 3
    if keys[pg.K_w] and y - 30 >= 0:
        y -= 3
    if keys[pg.K_s] and y + 30 <= HEIGHT:
        y += 3
    if keys[pg.K_SPACE]:
        COLOR = (rd.randint(0, 255), rd.randint(0, 255, ),  rd.randint(0, 255, ))
        t.sleep(0.2)


    screen.fill(MINT)
    pg.draw.circle(screen, COLOR, (x, y), r)

    pg.display.update()