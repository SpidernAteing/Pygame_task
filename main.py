import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600

SKY = (39, 245, 224)
GREEN = (27, 194, 36)
BROWN = (156, 110, 26)
DARK_BROWN = (117, 81, 19)
GLASS = (140, 255, 233)
BRICK = (189, 69, 6)
BLACK = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(SKY)
pg.display.set_caption("House")
clock = pg.time.Clock()

pg.draw.rect(screen, GREEN, (0, HEIGHT/2+150, WIDTH, HEIGHT/2-150))
pg.draw.rect(screen, BROWN, (WIDTH/2-200, HEIGHT/2-100, WIDTH/2-200, HEIGHT/2-50))
pg.draw.polygon(screen, BROWN, [[WIDTH/2-250, HEIGHT/2-100], [WIDTH/2-50, HEIGHT/2-250], [WIDTH/2+150, HEIGHT/2-100]])
pg.draw.lines(screen, BLACK, True, [[WIDTH/2-250, HEIGHT/2-100], [WIDTH/2-50, HEIGHT/2-250], [WIDTH/2+150, HEIGHT/2-100]], 3)
pg.draw.circle(screen, GLASS, [WIDTH/2-50, HEIGHT/2-165], 35)
pg.draw.circle(screen, DARK_BROWN, [WIDTH/2-50, HEIGHT/2-165], 35, 5)
pg.draw.line(screen, DARK_BROWN, [WIDTH/2-50, HEIGHT/2-195], [WIDTH/2-50, HEIGHT/2-135], 5)
pg.draw.line(screen, DARK_BROWN, [WIDTH/2-85, HEIGHT/2-165], [WIDTH/2-15, HEIGHT/2-165], 5)
pg.draw.line(screen, BLACK, [WIDTH/2-200, HEIGHT/2-100], [WIDTH/2-200, HEIGHT/2+150], 3)
pg.draw.line(screen, BLACK, [WIDTH/2+100, HEIGHT/2-100], [WIDTH/2+100, HEIGHT/2+150], 3)
pg.draw.rect(screen, DARK_BROWN, [WIDTH/2-175, HEIGHT/2-75, 75, 225])

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

    pg.display.update()