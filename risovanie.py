import pygame, time, random, settings,model

f = 1

def paint(screen):

    # рисуем кадр
    # f=f+1
    pygame.draw.rect(screen, [100, 250, 200], [0, 0, 1300, 700], 0)

    # pygame.draw.rect(screen, [0, 0, 0], w, 0)

    pygame.draw.rect(screen, [100, 200, 50], model.ok)

    pygame.draw.rect(screen, [f % 250, f % 200, f % 10], model.rect, 0)

    pygame.draw.circle(screen, [200, 0, 0], [model.w.centerx, model.w.centery], 20)
    pygame.display.flip()