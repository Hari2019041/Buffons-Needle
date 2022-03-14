import pygame
import random
import math

pygame.init()
pygame.font.init()

WIDTH = 1000
HEIGHT = 650
MARGIN = 60
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
    def __init__(self, no_of_needles=3_408):
        self.RUNNING = True
        self.no_of_needles = no_of_needles
        self.floor = Floor()
        self.needles = self.create_needles()
        self.probability = 0
        self.pi_estimate = 0

    def run(self):
        while self.RUNNING:
            SCREEN.fill(WHITE)
            for event in pygame.event.get():
                self.RUNNING = False if event.type == pygame.QUIT else True

            self.show_needles()
            self.floor.show_divisions()
            print(self.calculate_probability()**-1)
            pygame.display.update()

    def create_needles(self):
        needles = []
        for _ in range(self.no_of_needles):
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT-MARGIN)
            angle = random.uniform(0, 2*math.pi)
            needle = Needle(x, y, angle)
            needles.append(needle)
        return needles

    def show_needles(self):
        for needle in self.needles:
            needle.show()

    def calculate_probability(self):
        crossing_needles = 0
        for i, needle in enumerate(self.needles):
            start, end = needle.start, needle.end
            for j, line in enumerate(self.floor.divisions):
                x_left, x_right = min(start[0], end[0]), max(start[0], end[0])
                if x_left < line[0][0] < x_right:
                    needle.color = RED
                    crossing_needles += 1
        return crossing_needles/self.no_of_needles


class Needle:
    def __init__(self, x, y, angle, color=BLACK, length=50):
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
        pygame.draw.line(SCREEN, self.color, self.start, self.end)


class Floor:
    def __init__(self, width=100):
        self.width = width
        self.no_of_divisions = WIDTH//width
        self.divisions = self.create_divisions()

    def create_divisions(self):
        divisions = []
        for i in range(self.no_of_divisions+1):
            start = 100*i, 0
            end = 100*i, HEIGHT-MARGIN+30
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
