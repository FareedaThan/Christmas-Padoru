import pygame
class Bullet:
    def __init__(self,x,y,player_direction):
        self.image = pygame.image.load('eggplantshot.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = 1 if player_direction == "right" else -1

    def fire(self,):
        self.x += self.speed*self.direction
        self.rect = self.image.get_rect(center=(self.x, self.y))
        return self.image,self.rect

