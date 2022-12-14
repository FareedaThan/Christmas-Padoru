import pygame


class Player:
    def __init__(self):
        self.x = 100
        self.y = 400
        self.pos = self.x, self.y
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
        self.image = pygame.image.load('padoru.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,120))
        self.img_right = self.image
        self.img_left = pygame.transform.flip(self.image, True, False)
        self.direction = "right"

        self.isJump = False
        self.max_jump = 10
        self.jumpCount = self.max_jump
        self.max_bonce = 3
        self.bonce = self.max_bonce
        
    def move(self,move_speed):
        if self.left:
            self.x -= move_speed
            self.image = self.img_left
        elif self.right:
            self.x += move_speed
            self.image = self.img_right
        elif self.up:
            self.y -= move_speed
        elif self.down:
            self.y += move_speed
        elif self.isJump:
            self.jump()

    def stop(self):
        # called when you key up and stops the self
        self.left, self.right, self.up, self.down = 0, 0, 0, 0

    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump:
            if self.bonce > 0:
                if self.jumpCount >= int(-1*self.max_jump/2**(self.max_bonce-self.bonce)):
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= self.jumpCount ** 2 * 0.1 * neg
                    self.jumpCount -= 1
                    if self.bonce == self.max_bonce:
                        self.image = pygame.transform.flip(self.image, True, False) if self.jumpCount % 5 == 0 else self.image
                    if self.direction=="right":
                        self.x += 2
                    elif self.direction=="left":
                        self.x -= 2
                else:
                    self.bonce-=1
                    self.jumpCount = int(self.max_jump/2**(self.max_bonce-self.bonce))
                    if self.direction=="right":
                        self.image = self.img_right
                    elif self.direction=="left":
                        self.image = self.img_left
            else:
                self.isJump = False
                self.jumpCount = self.max_jump
                self.bonce=self.max_bonce

