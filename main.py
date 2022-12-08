import pygame
import main_class_game

def push(iteration, but):
    global f
    if iteration == 0:
        if but == 2:
            f = True
            return 1
    elif but == 1:
        f = True
        return 0
    else:
        return iteration


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    # ...
    # ...
    # смена (отрисовка) кадра:
    running = True
    iteration = 0
    f = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приёма и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                but = main_class_game.menu.prow((event.pos[0], event.pos[1]))
                if but == 3:
                    running = False
                # РЕАКЦИЯ НА ОСТАЛЬНЫЕ СОБЫТИЯ
                iteration = push(iteration, but)

            # ...
        if iteration == 0:
            if f:
                main_class_game.menu.initialization(screen)
                f = False
        else:
            if f:
                main_class_game.seting.initialization(screen)
                f = False
        pygame.display.flip()