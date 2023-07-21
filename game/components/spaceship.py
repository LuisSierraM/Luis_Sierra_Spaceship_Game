import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

class Spaceship(Sprite):
    SHIP_WIDTH = 40 #Ancho de la nave
    SHIP_HEIGHT = 60 #Altura de la nave
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH #Posicion horizontal donde aparece
    Y_POS = 500 #Posicion vertical donde aparece
    SHIP_SPEED = 10 #Velocidad

    def __init__(self):
        self.image = SPACESHIP #Imagen
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT)) #Se ajusta tamaño de imagen
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = "player" #Tipo de bala
        self.shoot = True #Habilitado para disparar
        self.power_up_type = DEFAULT_TYPE #Por defecto no tiene power up (Lista vacia)
        self.has_power_up = False 
        self.power_time_up = 0

    def shoot_bullet(self, game):
        bullet = Bullet(self) #Se crea el objeto y se añade a la lista de balas
        game.bullet_manager.add_bullet(bullet)
          
    def update(self, user_input, game): #Se establecen los controles y el limite de movimiento
        if user_input[pygame.K_LEFT]: #Movimiento hacia la izquierda
            if self.rect.left > 0:
                self.rect.x -= self.SHIP_SPEED
            else:
                self.rect.x = SCREEN_WIDTH - 40 

        if user_input[pygame.K_RIGHT]: #Movimiento hacia la derecha
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.SHIP_SPEED
            else:
                self.rect.x = 0  

        if user_input[pygame.K_UP]: #Movimiento hacia arriba
            if self.rect.y > SCREEN_HEIGHT // 2:
                self.rect.y -= self.SHIP_SPEED
                
        if user_input[pygame.K_DOWN]: #Movimiento hacia abajo
            if self.rect.y < SCREEN_HEIGHT - 70:
                self.rect.y += self.SHIP_SPEED

        if user_input[pygame.K_SPACE]: #Al presionar la tecla espacio se llama al metodo shoot_bullet, es decir, dispara
            self.shoot_bullet(game)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_image(self, size = (40,60), image = SPACESHIP): #Se le asigna la imagen
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
        
        
