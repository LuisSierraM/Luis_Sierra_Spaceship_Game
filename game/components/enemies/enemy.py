import pygame
from random import randint
from pygame.sprite import Sprite
from game.utils.constants import SHIP_WIDTH, SHIP_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    Y_POS = 20 #Constantes únicas del enemigo
    SPEED_X = 5
    SPEED_Y = 3
    MOVE_X = {0: "left", 1: "right"}
    SHOOT_INTERVAL = 1000

    def __init__(self, image):
        self.image = image #Se transforma el tamaño de la imagen a las medidas ancho y alto del ship (jugador)
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT)) 
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SCREEN_WIDTH)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOVE_X[randint(0, 1)]# 0 = izquierda, 1 = derecha. Esto es para el movimiento
        self.move_x_for = randint(30, 40)
        self.step = 0
        self.type = "enemy" #Tipo de bala / Propietario de la bala
        self.shooting_time = pygame.time.get_ticks() + randint(30, 50) #Tiempo de disparo

    def update(self, enemies, game):
        self.rect.y += self.speed_y #Movimiento vertical.
        self.shoot(game.bullet_manager) #Se llama al metodo shoot

        if self.movement_x == "left": #Movimiento horizontal
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT: #Se elimina al enemigo una vez que atraviesa el limite de la pantalla
            enemies.remove(self)

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if current_time >= self.shooting_time: #Implementacion de la logica para el disparo del enemigo
            bullet = Bullet(self) 
            bullet_manager.add_bullet(bullet)#Y añade una bala cuyo dueño es el enemigo a la lista.
            self.shooting_time = current_time + randint(20, 50)

    def draw(self, screen): #Se reflejan los cambios en la pantalla al actualizar
        screen.blit(self.image, self.rect)

    def change_movement_x(self): 
        self.step += 1
        if (self.step >= self.move_x_for and self.movement_x == "right") or (self.rect.x >= SCREEN_WIDTH - SHIP_WIDTH):
            self.movement_x = "left"
            self.step = 0
        #Aqui se implementa la logica para hacer que permanezcan dentro de la pantalla horizontalmente
        elif (self.step >= self.move_x_for and self.movement_x == "left") or (self.rect.x <= 5):
            self.movement_x = "right"
            self.step = 0

    def can_shoot(self): #Se verifica si esta habilitado para disparar de acuerdo al cooldown
        current_time = pygame.time.get_ticks() 
        if current_time >= self.shooting_time:
            self.shooting_time = current_time + self.SHOOT_INTERVAL
            return True
        return False
