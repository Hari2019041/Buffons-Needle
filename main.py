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
    def __init__(self, x, y, angle, color):
        self.length = 50
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
        pygame.draw.line(SCREEN, WHITE, self.start, self.end)


class Floor:
    def __init__(self):
        pass


def main():
    set_window(TITLE, ICON)
    simulation = Simulation()
    simulation.run()


if __name__ == '__main__':
    main()
