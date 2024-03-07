import math
import random
from math import cos, sin, sqrt
from random import randrange

import pygame

WIDTH = 800
HEIGHT = 800
CENTER = WIDTH // 2, HEIGHT // 2

G = 0.2
M = 10e7

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

r0 = 10  # Define r0 here

pygame.init()


class CelestialBody:
    def __init__(self, x, y, mass=2, momentum_x=500, momentum_y=500, dt=0.001):
        self.g = 0.2
        self.mass = mass
        self.x = x
        self.y = y
        self.momentum_x = momentum_x
        self.momentum_y = momentum_y
        self.dt = dt

    def move(self, central_mass):
        x2, y2 = central_mass
        hyp = math.hypot(self.x - x2, self.y - y2)
        theta = math.atan2(y2 - self.y, x2 - self.x)
        force = (self.g * self.mass * M) / hyp
        force_x = force * math.cos(theta)
        force_y = force * math.sin(theta)
        self.momentum_x += force_x * self.dt
        self.momentum_y += force_y * self.dt
        self.x += self.momentum_x / self.mass * self.dt
        self.y += self.momentum_y / self.mass * self.dt
        return [self.x, self.y]


def generator(shape='line'):
    particles = []
    if shape == 'line':
        for i in range(1000):
            x = randrange(-500, 1000)
            y = 100
            particles.append(CelestialBody(x, y))
    elif shape == 'circle':
        for i in range(1000):
            ang = random.uniform(0, 1) * 2 * math.pi
            hyp = sqrt(random.uniform(0, 1)) * r
            adj = cos(ang) * hyp
            opp = sin(ang) * hyp
            x = CENTER[0] + adj
            y = CENTER[1] + opp
            particles.append(CelestialBody(x, y))
    elif shape == 'square':
        for i in range(500):
            x = randrange(0, 500)
            y = randrange(0, 500)
            particles.append(CelestialBody(x, y))
    return particles


def draw(particles, screen):
    for particle in particles:
        pygame.draw.circle(screen, WHITE, (int(particle.move(CENTER)[0]), int(particle.move(CENTER)[1])), 1)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
particles = generator(shape='line')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Gravity point
    pygame.draw.circle(screen, WHITE, CENTER, r0)

    draw(particles, screen)

    pygame.display.update()
