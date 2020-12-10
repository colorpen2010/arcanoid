import pygame, time, settings, controller, model, risovanie

pygame.init()

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
# screen = pygame.display.set_mode([0,0],pygame.FULLSCREEN)

pygame.key.set_repeat(100, 100)  # залипание клавиши

#ставим иконку
block = pygame.image.load('cartinki/block 1.png')
block = pygame.transform.scale(block, [32, 32])
pygame.display.set_icon(block)
pygame.display.set_caption('arcanoid')

while 1 < 10:
    # задержа
    time.sleep(1 / 60)

    controller.obrabotca_sobitiy()

    model.dvizhenie()

    risovanie.paint(screen)