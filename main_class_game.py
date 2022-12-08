import pygame
import class_widgets
class Menu:
    def __init__(self):
        self.but1 = class_widgets.PushButton((300, 150), 'новая игра', 50, (0, 0, 0), pygame.Color(200, 200, 200, 50))
        self.but2 = class_widgets.PushButton((300, 250), 'настройки', 50, (0, 0, 0), pygame.Color(200, 200, 200, 50))
        self.but3 = class_widgets.PushButton((300, 350), 'выйти из игры', 50, (0, 0, 0), pygame.Color(200, 200, 200, 50))

    def initialization(self, screen):
        dog_surf = pygame.image.load('pictures/menu.png')
        dog_rect = dog_surf.get_rect(
            bottomright=(800, 600))
        screen.blit(dog_surf, dog_rect)

        pygame.display.update()
        self.but1.draw(screen)
        self.but2.draw(screen)
        self.but3.draw(screen)

    def prow(self, pos):
        if self.but1.prow(pos):
            return 1
        elif self.but2.prow(pos):
            return 2
        elif self.but3.prow(pos):
            return 3
        else:
            return 0



class Setings:
    def __init__(self):
        self.but1 = class_widgets.PushButton((300, 150), 'назад', 50, (0, 0, 0), (200, 200, 200, 50))

    def initialization(self, screen):
        dog_surf = pygame.image.load('pictures/menu.png')
        dog_rect = dog_surf.get_rect(
            bottomright=(800, 600))
        screen.blit(dog_surf, dog_rect)

        pygame.display.update()
        self.but1.draw(screen)

    def prow(self, pos):
        if self.but1.prow(pos):
            return 1
        else:
            return 0


menu = Menu()
seting = Setings()
