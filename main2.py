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

r = 30
x, y = rd.randint(0, WIDTH - r), rd.randint(0, HEIGHT - r)
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
        pressed = pg.mouse.get_pressed()
        if pressed[1] and x - r <= x1 <= x + r and y - r <= y1 <= y + r:
            x, y = rd.randint(0, WIDTH - r), rd.randint(0, HEIGHT - r)
            r = 30
        if pressed[0] and  y - r >= 0 and y + r <= HEIGHT and x - 30 >= 0 and x + r <= WIDTH:
            r += 3
        if pressed[2] and r > 3:
            r -= 3
        #if pg.MOU and y - r >= 0 and y + r <= HEIGHT and x - 30 >= 0 and x + r <= WIDTH:
            #r += 3
    if not flag_play:
        break

    x1, y1 = pg.mouse.get_pos()
    screen.fill(MINT)
    pg.draw.circle(screen, COLOR, (x, y), r)

    pg.display.update()