import pygame
import random
import math

pygame.init()
pygame.font.init()

WIDTH = 1000
HEIGHT = 600
MARGIN = 50
TITLE = 'Buffon\'s Needle Problem'
ICON = pygame.image.load('icon.png')
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (127, 127, 127)


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
            pygame.display.update()


class Needle:
    def __init__(self, x, y, angle, color, length=50):
        self.length = length
        self.x = x
        self.y = y
        self.start = (x, y)
        self.angle = angle
        self.end = self.find_end_point()
        self.color = color

    def find_end_point(self):
        new_x = self.x + self.length*math.cos(self.angle)
        new_y = self.y - self.length*math.sin(self.angle)
        return (new_x, new_y)

    def show(self):
        pygame.draw.line(SCREEN, BLACK, self.start, self.end)


class Floor:
    def __init__(self, no_of_divisions=10, width=100):
        self.no_of_divisions = no_of_divisions
        self.width = WIDTH//no_of_divisions
        self.divisions = self.create_divisions()

    def create_divisions(self):
        divisions = []
        for i in range(self.no_of_divisions+1):
            start = 100*i, 0
            end = 100*i, HEIGHT
            divisions.append((start, end))
        return divisions

    def show_divisions(self):
        for i, division in enumerate(self.divisions):
            start, end = division
            pygame.draw.line(SCREEN, GRAY, start, end)


def main():
    set_window(TITLE, ICON)
    simulation = Simulation()
    simulation.run()


if __name__ == '__main__':
    main()
