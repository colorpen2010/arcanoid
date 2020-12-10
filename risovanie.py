import pygame, time, random, settings,model


car_exit=pygame.image.load('cartinki/EXIT.png')
car_exit=pygame.transform.scale(car_exit,[100,50])
exit_rect=pygame.Rect(900,0,100,50)
def paint(screen):

    # рисуем кадр

    pygame.draw.rect(screen, [100, 250, 200], [0, 0, 1300, 700], 0)
    for security in model.blocks:
        pygame.draw.rect(screen,[100,250,50],security,10)

    pygame.draw.rect(screen, [250, 100, 10], model.platforma, 0)

    screen.blit(car_exit,exit_rect)

    # pygame.draw.rect(screen,[0,0,0],exit_rect)

    pygame.draw.circle(screen, [200, 0, 0], [model.krug.centerx, model.krug.centery], 20)
    pygame.display.flip()