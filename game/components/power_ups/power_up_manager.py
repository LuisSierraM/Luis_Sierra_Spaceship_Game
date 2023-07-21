import pygame

from random import randint

from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD


class PowerUpManager:

    def __init__(self):
        self.power_ups = [] #Lista vacia de power ups
        self.when_appears = randint(5000, 10000) #Aparece en un rango de 5 - 10 milisegundos
        self.duration = randint(3, 5) #Dura de 3 - 5 segundos

    def generate_power_up(self):
        power_up = Shield() #Se genera el power up
        self.when_appears += randint (5000, 10000)
        self.power_ups.append(power_up) #Se añade a la lista

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and  current_time >= self.when_appears:
            self.generate_power_up() #Se llama al metodo generate_power_up si se cumple la anterior condicion

        for power_up in self.power_ups: #Cada power up tendra una velocidad que es su caida atravez de la pantalla
            power_up.update(game.game_speed, self.power_ups) 
            if game.player.rect.colliderect(power_up):#Colision del power up con el jugador
                power_up.start_time = pygame.time.get_ticks() #Inicio del cronometro
                game.player.power_up_type = power_up.type 
                game.player.has_power_up = True #Se reconoce que el jugador tiene power up
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                game.player.set_image((65, 75), SPACESHIP_SHIELD) #Se cambia la imagen del jugador (Para hacer notar el power up)
                self.power_ups.remove(power_up) #Se remueve el power up

    def draw(self, screen): #Se dibuja
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self): #Se reinicia el power up (Vuelve a ser lista vacia)
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = randint(now + 5000, now + 10000)
