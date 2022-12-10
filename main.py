import pygame
import main_class_game

def push(iteration, but):
    global f
    if iteration == 1:
        if but == 2:
            f = True
            return 2
        else:
            return 1
    elif iteration == 2:
        if but == 1:
            f = True
            return 1
        else:
            return 2


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
    fps = 60
    clock = pygame.time.Clock()
    clock.tick(fps)
    while running:
        # внутри игрового цикла ещё один цикл
        # приёма и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                but = main_class_game.menu.prow((event.pos[0], event.pos[1]))
                if but == 3 and iteration == 1:
                    running = False
                # РЕАКЦИЯ НА ОСТАЛЬНЫЕ СОБЫТИЯ
                iteration = push(iteration, but)

            # ...
        if iteration == 0:
            main_class_game.Loading(screen)
            iteration = 1
        if iteration == 1:
            if f:
                main_class_game.menu.initialization(screen)
                f = False
        elif iteration == 2:
            if f:
                main_class_game.seting.initialization(screen)
                f = False

        pygame.display.flip()