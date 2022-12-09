import pygame
import random
import colorsys
import numpy as np
from Player import Player

# display set up
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()  # create object to help track time

# load image
bg_img = pygame.image.load('tree.png').convert_alpha()
bg_img = pygame.transform.scale(bg_img, (350, 350))

star_img = pygame.image.load('star.png').convert_alpha()
star_img = pygame.transform.scale(star_img, (120, 120))

dust_img = pygame.image.load('dust.png').convert_alpha()
dust_img = pygame.transform.scale(dust_img, (30, 30))

# player object
player = Player()

# constant
x_pos = 200
y_pos = 40

x_dust = 250
y_dust = 60

bound_L = 200
bound_R = 300
bound_U = 50
bound_D = 350
hor_speed = 5
ver_speed = 2
move_speed = 1
hor_direction = 1
ver_direction = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Set color to image
def set_color(img, color):
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            color.a = img.get_at((x, y)).a  # Preserve the alpha value.
            img.set_at((x, y), color)


# Indicates where the player is directed
def get_key(event):
    # checks which key you pressed
    if event.key == pygame.K_LEFT:
        return "left"
    elif event.key == pygame.K_RIGHT:
        return "right"
    elif event.key == pygame.K_UP:
        return "up"
    elif event.key == pygame.K_DOWN:
        return "down"


while True:
    if player.left:
        player.x -= move_speed
        player.image = player.img_left
    elif player.right:
        player.x += move_speed
        player.image = player.img_right
    elif player.up:
        player.y -= move_speed
    elif player.down:
        player.y += move_speed
    elif player.isJump:
        player.jump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if get_key(event) == "left":
                player.left = 1
                player.right = 0
                player.direction = "left"
            elif get_key(event) == "right":
                player.right = 1
                player.left = 0
                player.direction = "right"
            elif get_key(event) == "up":
                player.up = 1
                player.down = 0
            elif get_key(event) == "down":
                player.down = 1
                player.up = 0
            elif event.key == pygame.K_SPACE:
                # Start to jump by setting isJump to True.
                player.isJump = True

        elif event.type == pygame.KEYUP:
            player.stop()

    screen.fill(BLACK)
    screen.blit(bg_img, (75, 75))

    r, g, b = colorsys.hsv_to_rgb(0.15, random.uniform(0.99, 1.0), random.uniform(0.9, 1))
    set_color(star_img, pygame.Color(round(r*255), round(g*255), round(b*255)))
    # rect = image.get_rect(center=(x_pos, y_pos))  # suppose to be the position of start point
    screen.blit(star_img, (x_pos, y_pos))
    screen.blit(dust_img, (x_dust, y_dust))
    screen.blit(player.image, (player.x, player.y))

    if x_dust >= bound_R or x_dust <= bound_L:
        hor_direction *= -1
    if y_dust >= bound_D or y_dust <= bound_U:
        ver_direction *= -1

    x_dust += hor_speed * hor_direction
    y_dust += ver_speed * ver_direction

    pygame.display.update()
    clock.tick(40)
