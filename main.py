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

def flip(spites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

#Loading image
def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alfa()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(i * width, 0, width, height)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alfa()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.stransform.scale2x(surface)

#Speler maken
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCaracters", "MaskDude", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_speed = 0
        self.y_speed = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

#bewegen naar links
    def move_left(self, speed):
        self.x_speed = -speed
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

#bewegen naar rechts
    def move_right(self, speed):
        self.x_speed = speed
         if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_speed += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_speed, self.y_speed)

        self.fall_count += 1
        self.update_sprite()

    #Image animating
    def update_sprite(self):
        sprite_sheet = "idle"
        if self.x_speed != 0:
            sprite_sheet = "run"
        
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(spites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, window):
        win.blit(self.sprite, (self.rect.x, self.rect.y))


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Block(Object):
    def __init__(self, x, y, size):
         super().__init__(x, y, size, size)
         block = get.block(size)
         self.image.blit(block, (0, 0))
         self.mask = pygame.mask.from_surface(self.image)


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
def draw(window, background, bg_image, player, objects):
    for tile in background:
        window.blit(bg_inage, tile)

    for obj in objects:
        obj.draw(window)

    player.draw(window)

    pygame.display.update()

#Speler bewegen
def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_speed = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_SPEED)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_SPEED)

#Achtergrond
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("galaxy.png")

    block_size = 96

    player = Player(100, 100, 50, 50)
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]


#While loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player, floor)  
    
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
