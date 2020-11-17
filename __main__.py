import pygame, time, random, settings

pygame.init()
f = 1

pygame.key.set_repeat(100, 100)

speedy = 1
speedx = 1
screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
rect = pygame.Rect(70, 400, 200, 20)
w = pygame.Rect(200, 200, 40, 40)
while 1 < 10:

    # задержа
    time.sleep(1 / 60)

    # обработка событий
    coffin_dance = pygame.event.get()

    for e in coffin_dance:
        if e.type == pygame.MOUSEMOTION:
            #в право
            sdvigx=e.pos[0]-rect.centerx
            if sdvigx >= 1:
                rect.x += sdvigx
                e1 = rect.colliderect(w)
                if e1 == 1:
                    rect.right = w.left
            #в лево
            if sdvigx <= -1:
                rect.x -= 20
                e1 = rect.colliderect(w)
                if e1 == 1:
                    rect.left = w.right

        if e.type == pygame.KEYDOWN:
            # if e.key == pygame.K_UP:
            #     rect.y -= 20
            #     e1 = rect.colliderect(w)
            #     if e1 == 1:
            #         rect.y = w.bottom
            #
            # if e.key == pygame.K_DOWN:
            #     rect.y += 20
            #     e1 = rect.colliderect(w)
            #     if e1 == 1:
            #         rect.bottom = w.y

            if e.key == pygame.K_RIGHT:
                rect.x += 20
                e1 = rect.colliderect(w)
                if e1 == 1:
                    rect.right = w.left

            if e.key == pygame.K_LEFT:
                rect.x -= 20
                e1 = rect.colliderect(w)
                if e1 == 1:
                    rect.left = w.right

    # границы для прямоуголльника 1
    if rect.y < 0:
        rect.y = 0
    if rect.x < 0:
        rect.x = 0
    if rect.right > 800:
        rect.right = 800
    if rect.bottom > 700:
        rect.bottom = 700

    # движение шарика
    w.x += speedx

    # грницы для круга
    if w.right > settings.SCREEN_WIDTH:
        w.right = settings.SCREEN_WIDTH
        speedx = -7
    if w.x < 0:
        w.x = 0
        speedx = 7

    # твердый прямоугольник
    e1 = rect.colliderect(w)
    if e1 == 1 and speedx > 0:
        speedx = - 7
        w.right = rect.x
    elif e1 == 1 and speedx < 0:
        speedx = 7
        w.x = rect.right

    w.y += speedy
    if w.bottom > settings.SCREEN_HEIGHT:
        w.bottom = settings.SCREEN_HEIGHT
        speedy = - 7
    if w.top < 0:
        w.top = 0
        speedy = 7

    e1 = rect.colliderect(w)
    if e1 == 1 and speedy > 0:
        speedy = - 7
        w.bottom = rect.y
    elif e1 == 1 and speedy < 0:
        speedy = 7
        w.y = rect.bottom

        # рисуем кадр
    # f=f+1
    pygame.draw.rect(screen, [100, 250, 200], [0, 0, 1300, 700], 0)

    # pygame.draw.rect(screen, [0, 0, 0], w, 0)

    pygame.draw.rect(screen, [f % 250, f % 200, f % 10], rect, 0)

    pygame.draw.circle(screen, [200, 0, 0], [w.centerx, w.centery], 20)
    pygame.display.flip()
