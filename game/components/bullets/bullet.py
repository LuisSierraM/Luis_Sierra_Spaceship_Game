import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET, (10, 25)) #Tamaño de la bala
    BULLET_SIZE_ENEMY = pygame.transform.scale(BULLET_ENEMY, (9, 32)) #Tamaño de la bala del enemigo
    BULLETS = {"player": BULLET_SIZE, "enemy": BULLET_SIZE_ENEMY} #Tipos de bala
    SPEED = 20 #Velocidad de la bala

    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

    def update(self, bullets):
        if self.owner == 'player': #Movimiento de la bala del jugador
            self.rect.y -= self.SPEED
        else: #Movimiento de la bala del enemigo
            self.rect.y += self.SPEED
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT: #Cada bala que se salga de la pantalla
            bullets.remove(self) #Sera eliminada

    def draw(self, screen): #Se dibuja
        screen.blit(self.image, self.rect)

