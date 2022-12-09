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
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.img_right = self.image
        self.img_left = pygame.transform.flip(self.image, True, False)
        self.direction = "right"

        self.isJump = False
        self.jumpCount = 10

    def stop(self):
        # called when you key up and stops the player
        self.left, self.right, self.up, self.down = 0, 0, 0, 0

    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount ** 2 * 0.1 * neg
                self.jumpCount -= 1
                self.image = pygame.transform.flip(self.image, True, False)
                if self.direction=="right":
                    self.x += 1
                elif self.direction=="left":
                    self.x -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

