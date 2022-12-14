import pygame
class Bullet:
    def __init__(self,x,y,player_direction,type):
        self.image = pygame.image.load('eggplantshot.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,60))
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = 1 if player_direction == "right" else -1
        self.count = 10
        self.type = type

    def fire(self):
        if self.type == "fire":
            self.x += self.speed*self.direction
        elif self.type == "throw":
            if self.y<=420:
                neg = 1
                if self.count < 0:
                    neg = -1
                self.y -= self.count ** 2 * 0.1 * neg
                self.count -= 1
                self.x += 4*self.direction
        self.rect = self.image.get_rect(center=(self.x, self.y))
        return self.image,self.rect
