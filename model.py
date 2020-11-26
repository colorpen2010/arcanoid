import pygame, settings

# подготовка модэли
ok = pygame.Rect(100, 100, 300, 150)

platforma = pygame.Rect(50, 400, 200, 20)
platforma.centerx = settings.SCREEN_WIDTH / 2
krug = pygame.Rect(70, 300, 40, 40)

speedy = 1
speedx = 1


def platformirovanie():
    platforma.x += 20
    e1 = platforma.colliderect(krug)
    if e1 == 1:
        platforma.right = krug.left


def dvizhenie():
    global speedx, speedy

    # границы для прямоуголльника 1
    if platforma.y < 0:
        platforma.y = 0
    if platforma.x < 0:
        platforma.x = 0
    if platforma.right > settings.SCREEN_WIDTH:
        platforma.right = settings.SCREEN_WIDTH
    if platforma.bottom > settings.SCREEN_HEIGHT:
        platforma.bottom = settings.SCREEN_HEIGHT

    # движение шарика
    krug.x += speedx

    # грницы для круга
    if krug.right > settings.SCREEN_WIDTH:
        krug.right = settings.SCREEN_WIDTH
        speedx = -7
    if krug.x < 0:
        krug.x = 0
        speedx = 7

    # твердый прямоугольник
    e1 = platforma.colliderect(krug)
    if e1 == 1 and speedx > 0:
        speedx = - 7
        krug.right = platforma.x
    elif e1 == 1 and speedx < 0:
        speedx = 7
        krug.x = platforma.right

    krug.y += speedy
    if krug.bottom > settings.SCREEN_HEIGHT:
        krug.bottom = settings.SCREEN_HEIGHT
        speedy = - 7
    if krug.top < 0:
        krug.top = 0
        speedy = 7

    e1 = platforma.colliderect(krug)
    if e1 == 1 and speedy > 0:
        speedy = - 7
        krug.bottom = platforma.y
    elif e1 == 1 and speedy < 0:
        speedy = 7
        krug.y = platforma.bottom
