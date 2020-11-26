import pygame, model


def obrabotca_sobitiy():
    # обработка событий
    coffin_dance = pygame.event.get()

    for e in coffin_dance:
        # if e.type == pygame.MOUSEMOTION:
        #     в право
        # sdvigx = e.pos[0] - rect.centerx
        # if sdvigx >= 1:
        #     rect.x += sdvigx
        #     e1 = rect.colliderect(w)
        #     if e1 == 1:
        #         rect.right = w.left
        # в лево
        # if sdvigx <= -1:
        #     rect.x -= 20
        #     e1 = rect.colliderect(w)
        #     if e1 == 1:
        #         rect.left = w.right

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_RIGHT:
                model.platformirovanie()

            if e.key == pygame.K_LEFT:
                model.platforma.x -= 20
                e1 = model.platforma.colliderect(model.krug)
                if e1 == 1:
                    model.platforma.left = model.krug.right