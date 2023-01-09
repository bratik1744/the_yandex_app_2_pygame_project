import pygame
import main_class_game
import space


def push(iteration, pos):
    global f
    global running
    if iteration == 0:
        return 0
    if iteration == 1:
        but = main_class_game.menu.prow(pos)
        if but == 2:
            f = True
            return 2
        elif but == 1:
            f = True
            return 3
        elif but == 3:
            running = False
            return 1
        else:
            return 1
    elif iteration == 2:
        but = main_class_game.seting.prow(pos)
        if but == 1:
            f = True
            return 1
        elif but == 2:
            file = main_class_game.prompt_file()
            fil = open('mode.txt', 'w')
            fil.write(file)
            fil.close()
            f = True
            return 1
        else:
            return 2
    elif iteration == 3:
        return 3
    elif iteration == 4:
        but = main_class_game.game.prow(pos)
        if but == 1:
            running = False
            return 4
        elif but == -1:
            return 4
        else:
            f = True
            return 4


def ff():
    global f
    f = True


if __name__ == '__main__':
    fil = open('mode.txt', 'w')
    fil.write('plot.db')
    fil.close()
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
                if (but == 3 and iteration == 1) or ((but == 3 and iteration == 1)):
                    running = False
                # РЕАКЦИЯ НА ОСТАЛЬНЫЕ СОБЫТИЯ
                iteration = push(iteration, (event.pos[0], event.pos[1]))

            # ...
        if iteration == 0:
            #main_class_game.Loading(screen)
            iteration = 1
        if iteration == 1:
            if f:
                main_class_game.menu.initialization(screen)
                f = False
        elif iteration == 2:
            if f:
                main_class_game.seting.initialization(screen)
                f = False
        elif iteration == 3:
            #space.f()
            iteration = 4
        elif iteration == 4:
            if f:
                main_class_game.game.initialization(screen)
                f = False


    pygame.display.flip()



