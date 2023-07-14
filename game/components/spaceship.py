import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - 40
        self.rect.y = 500

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= 10
        elif user_input[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += 10
        elif user_input[pygame.K_UP]:
            if self.rect.y > SCREEN_HEIGHT // 2:
                self.rect.y -= 10
        elif user_input[pygame.K_DOWN]:
            if self.rect.y < SCREEN_HEIGHT -70:
                self.rect.y += 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        

        
