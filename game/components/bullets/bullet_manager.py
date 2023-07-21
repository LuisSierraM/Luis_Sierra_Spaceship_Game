import pygame
from game.components.bullets.bullet import Bullet

class BulletManager:
    def __init__(self):
        self.bullets = [] #Lista de balas del jugador
        self.enemy_bullets = [] #Lista de balas de los enemigos

    def update(self, game):
        bullets_copy = self.bullets.copy()
        enemy_bullets_copy = self.enemy_bullets.copy()

        for bullet in bullets_copy: #Cada bala que se haya copiado se actualiza
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner != 'enemy': #Se implementa la colision
                    game.enemy_manager.enemies.remove(enemy) #Y se elimina al enemigo de la lista
                    if bullet in self.bullets:
                        self.bullets.remove(bullet) #Tambien se elimina la bala ya que ha colisionado
                    game.score += 1 #Se le suma puntaje al jugador
                    game.enemy_manager.enemy_died() #Se llama al metodo enemy_died para aumentar el enemy_count y 
                                                    #Que apareazcan más enemigos

        for bullet in enemy_bullets_copy:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy": #Colision de bala enemiga con el jugador
                if bullet in self.enemy_bullets: 
                    self.enemy_bullets.remove(bullet) #Se elimina la bala que colisionó
                if not game.player.has_power_up: #Si el jugador no tiene power up (Escudo)
                    game.playing = False #Se acaba el juego (Muere)
                    game.death_count += 1 #Se le suma una muerte al contador.
                    pygame.time.delay(1000)
                    break

    def draw(self, screen):
        for bullet in self.bullets: #Cada bala tanton del enemigo, como del jugador
            bullet.draw(screen) #Se mostrara en la pantalla
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.bullets) < 5: #Aqui es cuando se añaden las balas a la lista
            self.bullets.append(bullet) #Del enemigo y del jugador
        elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 10: #Numero de balas en pantalla.
            self.enemy_bullets.append(bullet)

        
            