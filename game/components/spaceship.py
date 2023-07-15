import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.SHIP_SPEED
            else:
                self.rect.x = SCREEN_WIDTH - 40 

        if user_input[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.SHIP_SPEED
            else:
                self.rect.x = 0  

        if user_input[pygame.K_UP]:
            if self.rect.y > SCREEN_HEIGHT // 2:
                self.rect.y -= self.SHIP_SPEED
                
        if user_input[pygame.K_DOWN]:
            if self.rect.y < SCREEN_HEIGHT - 70:
                self.rect.y += self.SHIP_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
