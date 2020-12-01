import pygame, settings

# подготовка модэли
ok = pygame.Rect(100, 100, 300, 150)

platforma = pygame.Rect(50, 400, 200, 20)
platforma.centerx = settings.SCREEN_WIDTH / 2
krug = pygame.Rect(70, 300, 40, 40)

speedy = 1
speedx = 1


def platforma_right():
    platforma.x += 20
    e1 = platforma.colliderect(krug)
    if e1 == 1:
        platforma.right = krug.left


def platforma_left():
    platforma.x -= 20
    e1 = platforma.colliderect(krug)
    if e1 == 1:
        platforma.left = krug.right


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

    otbivka_left_right(ok)

    otbivka_left_right(platforma)

    krug.y += speedy
    if krug.bottom > settings.SCREEN_HEIGHT:
        krug.bottom = settings.SCREEN_HEIGHT
        speedy = - 7
    if krug.top < 0:
        krug.top = 0
        speedy = 7

    otbivka_top_bottom(platforma)

    otbivka_top_bottom(ok)

def otbivka_left_right(block):
    global speedx, speedy
    e1 = block.colliderect(krug)
    if e1 == 1 and speedx > 0:
        speedx = - 7
        krug.right = block.x
    elif e1 == 1 and speedx < 0:
        speedx = 7
        krug.x = block.right


def otbivka_top_bottom(block):
    global speedx, speedy

    e1 = block.colliderect(krug)
    if e1 == 1 and speedy > 0:
        speedy = - 7
        krug.bottom = block.y
    elif e1 == 1 and speedy < 0:
        speedy = 7
        krug.y = block.bottom
