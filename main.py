import random

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Shooting Gallery Game")
icon = pygame.image.load("Img/apple.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("Img/apple.jpg")
target_width = 100
target_height = 100
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (0, 20, 0)

running = True
while running:
    pass




pygame.quit()