import pygame as pg

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

speed = 2
x = 0
y = WIN_HEIGHT // 2
pg.draw.rect(screen, ORANGE, (x, y-25, 50, 50))
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


    if x >= WIN_WIDTH:
        x -= 50
        speed = -speed
        y = WIN_HEIGHT // 2
        square_left = 50
        flag = False
    else:
        x += speed



    screen.fill(WHITE)
    pg.draw.rect(screen, ORANGE, (x, y-25, 50, 50))
    pg.display.update()