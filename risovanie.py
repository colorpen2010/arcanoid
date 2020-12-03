import pygame, time, random, settings,model



def paint(screen):

    # рисуем кадр
    # pygame.draw.rect(screen, [100, 250, 200], [0, 0, 1300, 700], 0)

    # pygame.draw.rect(screen, [100, 200, 50], model.blocks[0])
    for security in model.blocks:
        pygame.draw.rect(screen,[100,250,50],security,5)

    pygame.draw.rect(screen, [250, 100, 10], model.platforma, 0)

    pygame.draw.circle(screen, [200, 0, 0], [model.krug.centerx, model.krug.centery], 20)
    pygame.display.flip()