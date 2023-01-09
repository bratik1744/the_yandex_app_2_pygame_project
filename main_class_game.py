import pygame
import pygame
import class_widgets
import sqlite3
import tkinter
import tkinter.filedialog
import sys

import main


def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name

class Menu:
    def __init__(self):
        self.but1 = class_widgets.PushButton((300, 150), 'новая игра', 50, (0, 0, 0), pygame.Color(200, 200, 200))
        self.but2 = class_widgets.PushButton((300, 250), 'настройки', 50, (0, 0, 0), pygame.Color(200, 200, 200))
        self.but3 = class_widgets.PushButton((300, 350), 'выйти из игры', 50, (0, 0, 0), pygame.Color(200, 200, 200))

    def initialization(self, screen):
        dog_surf = pygame.image.load('pictures/menu.jpg')
        dog_rect = dog_surf.get_rect(
            bottomright=(800, 600))
        screen.blit(dog_surf, dog_rect)

        pygame.display.update()
        self.but1.draw(screen)
        self.but2.draw(screen)
        self.but3.draw(screen)
        pygame.display.update()

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
        self.but2 = class_widgets.PushButton((300, 250), 'запустить мод', 50, (0, 0, 0), (200, 200, 200, 50))

    def initialization(self, screen):
        dog_surf = pygame.image.load('pictures/menu.png')
        dog_rect = dog_surf.get_rect(
            bottomright=(800, 600))
        screen.blit(dog_surf, dog_rect)

        pygame.display.update()
        self.but1.draw(screen)
        self.but2.draw(screen)
        pygame.display.update()

    def prow(self, pos):
        if self.but1.prow(pos):
            return 1
        elif self.but2.prow(pos):
            return 2
        else:
            return 0

class Loading:
    def __init__(self, screen):
        progress = 0
        run = True
        pygame.draw.rect(screen, (255, 255, 255), (50, 500, 700, 50), 1)
        while progress < 630:
            self.draw(progress, screen)
            progress += 0.1

    def draw(self, progress, screen):
        #screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), (50, 500, 70 + int(progress), 50), 0)
        pygame.display.flip()


class Game:
    def __init__(self):
        self.but1 = class_widgets.PushButton((300, 0), 'выйти из игры', 50, (0, 0, 0), pygame.Color(200, 200, 200))
        self.id_dialog = 0
        self.id_branching = 0
        self.lst_but = []
        self.branching_next = []

    def initialization(self, screen):
        f = open('mode.txt', 'r')
        plot = f.readline()
        f.close()
        con = sqlite3.connect(plot)
        cur = con.cursor()
        branching = cur.execute(f"SELECT * FROM branching_main WHERE id = '{self.id_branching}'").fetchall()
        hist = cur.execute(f"SELECT * FROM {branching[0][1]} WHERE id = '{self.id_dialog}'").fetchall()
        #print(hist)
        if not hist[0][7]:
            self.id_dialog += 1
            if not hist[0][9]:
                dog_surf = pygame.image.load(hist[0][3])
                dog_rect = dog_surf.get_rect(
                    bottomright=(800, 600))
                screen.blit(dog_surf, dog_rect)
                pygame.draw.rect(screen, (200, 200, 200), (0,  500, 800, 600), 0)
                font = pygame.font.Font(None, 40)
                text = font.render(hist[0][1], True, (0, 0, 0))
                text2 = font.render(hist[0][2], True, (0, 0, 0))
                screen.blit(text, (20, 550))
                screen.blit(text2, (300, 500))
                self.but1.draw(screen)
                if hist[0][4]:
                    self.lst_but = []
                    lst_choice = hist[0][5].split('/')
                    self.branching_next = list(map(int, hist[0][6].split('/')))
                    for i in range(len(lst_choice)):
                        self.lst_but.append(class_widgets.PushButton((300, 75 + 75 * i), lst_choice[i], 50, (0, 0, 0), pygame.Color(200, 200, 200)))

                    for i in self.lst_but:
                        i.draw(screen)
                pygame.display.update()
            else:
                sys.path.insert(0, f"{hist[0][10]}")
                exec(f'import {hist[0][11]}')
                main.ff()
        else:
            screen.fill((255, 255, 255))
            end = cur.execute(f"SELECT * FROM end WHERE id = '{hist[0][8]}'").fetchall()
            end_txt = end[0][1]
            font = pygame.font.Font(None, 40)
            text = font.render(end_txt, True, (0, 0, 0))
            screen.blit(text, (20, 300))
            self.but1.draw(screen)
            pygame.display.update()

    def prow(self, pos):
        if self.but1.prow(pos):
            return 1
        elif self.lst_but:
            for i in range(len(self.lst_but)):
                if self.lst_but[i].prow(pos):
                    self.id_dialog = 0
                    self.id_branching = self.branching_next[i]
                    self.lst_but = []
                    self.branching_next = []
                    return 0
            return -1
        else:
            return 0





menu = Menu()
seting = Setings()
game = Game()
