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

#Speler maken
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)



    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

#bewegen naar links
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

#bewegen naar rechts
    def move_right(self, vel):
        self.x_vel = vel
         if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)


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
def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_inage, tile)

    player.draw(window)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("galaxy.png")

    player = Player(100, 100, 50, 50)

#While loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, background, bg_image, player)  
    
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
