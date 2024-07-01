import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("platformer")

WIDTH, HEIGHT = 250, 250
FPS = 60
PLAYER_SPEED = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

#Achtergrond gaat over de hele scherm
def get_background(name):
    image = pygame.image.load(join("achtergrond", "galaxy.png"))
    _, _, width, height = image.get_rect()
    tiles = []

     for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image


#Steeds nieuwe achtergrond tekenen bij elke beweging
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_inage, tile)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("galaxy.png")

#While loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, background, bg_image)  
    
    #Juiste fps
    clock.tick(FPS)
    
    pygame.quit()
    quit()


    # Keyboard inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()




if __name__ == "__main__":
    main(window)
