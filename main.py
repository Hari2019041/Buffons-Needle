import pygame
import random
import math

pygame.init()
pygame.font.init()

WIDTH = 900
HEIGHT = 600
MARGIN = 50
TITLE = 'Buffon\'s Needle Problem'
ICON = pygame.image.load('icon.png')
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def set_window(TITLE, ICON):
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)


class Simulation:
    def __init__(self):
        self.RUNNING = True

    def run(self):
        while self.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False


class Needle:
    def __init__(self):
        pass


class Floor:
    def __init__(self):
        pass


def main():
    set_window(TITLE, ICON)
    simulation = Simulation()
    simulation.run()


if __name__ == '__main__':
    main()
