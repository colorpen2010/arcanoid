import pygame, time, random, settings,controller,model,risovanie

pygame.init()


pygame.key.set_repeat(100, 100)
block = pygame.image.load('cartinki/block 1.png')

# block=pygame.transform.scale(block,[settings.BLOCK_WIDTH,settings.BLOCK_HEIGHT])
block = pygame.transform.scale(block, [32, 32])

screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])

pygame.display.set_icon(block)
pygame.display.set_caption('arcanoid')

while 1 < 10:

    # задержа
    time.sleep(1 / 60)

    controller.obrabotca_sobitiy()

    model.dvizhenie()

    risovanie.paint(screen)