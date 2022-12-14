import pygame
import random
import colorsys
import pyautogui
import numpy as np
from Player import Player, Enemy
from pygame import mixer
import os
from Song import ThemeSong
from Bullet import Bullet
from random import randint
os.chdir(r"Christmas-Padoru")
# display set up
pygame.init()
font = pygame.font.Font("ELEPHNTI.TTF",36)
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()  # create object to help track time

# load image
bg_img = pygame.image.load('tree.png').convert_alpha()
bg_img = pygame.transform.scale(bg_img, (370, 370))

star_img = pygame.image.load('star.png').convert_alpha()
star_img = pygame.transform.scale(star_img, (120, 120))

dust_img = pygame.image.load('dust.png').convert_alpha()
dust_img = pygame.transform.scale(dust_img, (30, 30))

# load & play Sound
# mixer.music.load("Padoru_Song.wav")
# mixer.music.set_volume(0)
# mixer.music.play(-1)
themesong = ThemeSong()
lyrics = themesong.play()
fire = False
# player object
player = Player()
boss = Enemy()

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

bullet_list=[]
while True:
    player.move(move_speed)
    boss.move(randint(-1,3)*(player.x-boss.x)/(abs(player.x-boss.x)))
    MUSIC_END = pygame.USEREVENT+1
    pygame.mixer.music.set_endevent(MUSIC_END)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == MUSIC_END:
            lyrics = themesong.play()
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
                jump_sound = mixer.Sound("jump.wav")
                jump_sound.set_volume(.2)
                mixer.Sound.play(jump_sound)
            elif event.key == pygame.K_s:
                # Get sound
                mixer.music.set_volume(.05)
            elif event.key == pygame.K_d:
                # mute sound
                mixer.music.set_volume(0)
            elif event.key == pygame.K_c:
                # fire
                bullet_list.append(Bullet(player.x,player.y,player.direction,"fire"))
                fire_sound = mixer.Sound("shoot.wav")
                fire_sound.set_volume(.2)
                mixer.Sound.play(fire_sound)
            elif event.key == pygame.K_x:
                # bomb
                bullet_list.append(Bullet(player.x,player.y,player.direction,"throw"))
                fire_sound = mixer.Sound("shoot.wav")
                fire_sound.set_volume(.2)
                mixer.Sound.play(fire_sound)
            elif event.key == pygame.K_q:
                # bomb
                player.restart()
                boss.restart()
                
        elif event.type == pygame.KEYUP:
            player.stop()

    screen.fill(BLACK)
    bg_rect = bg_img.get_rect(center=(500/2, 500/2))
    screen.blit(bg_img,bg_rect)

    r, g, b = colorsys.hsv_to_rgb(0.15, random.uniform(0.99, 1.0), random.uniform(0.9, 1))
    set_color(star_img, pygame.Color(round(r*255), round(g*255), round(b*255)))
    # rect = image.get_rect(center=(x_pos, y_pos))  # suppose to be the position of start point
    
    text_display=font.render(lyrics,True,"red")
    text_rect = text_display.get_rect(center=(500/2, 40))
    player_rect = player.image.get_rect(center=(player.x, player.y))
    boss_rect = boss.image.get_rect(center=(boss.x, boss.y))
    
    screen.blit(text_display,text_rect)
    screen.blit(star_img, (x_pos, y_pos))
    screen.blit(dust_img, (x_dust, y_dust))
    screen.blit(player.image, player_rect)
    screen.blit(boss.image, boss_rect)
    for bullet in bullet_list:
        if abs(bullet.x-boss.x) <= 50:
            fire_sound = mixer.Sound("hit.wav")
            fire_sound.set_volume(.5)
            mixer.Sound.play(fire_sound)
            bullet_list.remove(bullet)
            boss.damaged()
        else:
            if bullet.time >= 25:
                bullet_list.remove(bullet)
            else:
                screen.blit(*bullet.fire())

    if x_dust >= bound_R or x_dust <= bound_L:
        hor_direction *= -1
    if y_dust >= bound_D or y_dust <= bound_U:
        ver_direction *= -1

    x_dust += hor_speed * hor_direction
    y_dust += ver_speed * ver_direction

    if abs(player.x-boss.x) <= 50 and boss.status == "a":
        pyautogui.alert("padoru padoru")
        player.restart()
        boss.restart()
    pygame.display.update()
    clock.tick(40)
    
    
