import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("platformer")

BG_COLOR = (255,255,255)
WIDTH, HEIGHT = 250, 250
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


def main(window):
    clock = pygame.time.Clock()

#Deze code hieronder zorgt ervoor dat de game niet meer dan het aantal ingestelde fps (in dit geval 60) runt.
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    clock.tick(FPS)

    # Keyboard inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()



if __name__ == "__main__":
    main(window)
