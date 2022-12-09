import pygame


class PushButton:
    def __init__(self, pos, text, fnt, clr_text, clr_contour):
        self.pos = pos
        self.text = text
        self.fnt = fnt
        self.clr_text = clr_text
        self.clr_contour = clr_contour


    def draw(self, screen):
        font = pygame.font.Font(None, self.fnt)
        text = font.render(self.text, True, self.clr_text)
        self.text_x = self.pos[0]
        self.text_y = self.pos[1]
        self.text_w = text.get_width()
        self.text_h = text.get_height()
        pygame.draw.rect(screen, self.clr_contour, (self.text_x - 10, self.text_y - 10,
                                                    self.text_w + 20, self.text_h + 20), 0)
        screen.blit(text, (self.text_x, self.text_y))


    def prow(self, pos):
        if self.text_x - 10 <= pos[0] <= self.text_x + self.text_w + 10 and self.text_y - 10 <= pos[1] <= self.text_y + self.text_h + 10:
            return True
        else:
            return False


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