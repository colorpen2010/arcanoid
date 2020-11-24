import pygame, time, random, settings

#подготовка модэли
ok = pygame.Rect(100, 100, 300, 150)

rect = pygame.Rect(50, 400, 200, 20)
rect.centerx = settings.SCREEN_WIDTH / 2
w = pygame.Rect(70, 300, 40, 40)

speedy = 1
speedx = 1

def platformirovanie():
    rect.x += 20
    e1 = rect.colliderect(w)
    if e1 == 1:
        rect.right = w.left


def dvizhenie():

    global speedx,speedy

    # границы для прямоуголльника 1
    if rect.y < 0:
        rect.y = 0
    if rect.x < 0:
        rect.x = 0
    if rect.right > settings.SCREEN_WIDTH:
        rect.right = settings.SCREEN_WIDTH
    if rect.bottom > settings.SCREEN_HEIGHT:
        rect.bottom = settings.SCREEN_HEIGHT

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