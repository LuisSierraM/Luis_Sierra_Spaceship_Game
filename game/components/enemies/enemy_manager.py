import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2
from game.components.bullets.bullet import Bullet

class EnemyManager:
    def __init__(self):
        self.enemies = [] #Lista de enemigos
        self.enemy_count = 0 #Contador de enemigos

    def update(self, game):
        self.add_enemy() #Llamamos al metodo add_enemy

        for enemy in self.enemies: #Cada enemigo que este en la lista se llama su metodo update
            enemy.update(self.enemies, game) #Para actualizar su movimiento
            if enemy.can_shoot():
                bullet = Bullet(enemy) #Si el enemigo puede disparar se añade una bala teniendo como propietario
                game.bullet_manager.add_bullet(bullet) #El mismo enemigo

    def draw(self, screen):
        for enemy in self.enemies: #Este metodo "dibuja" a los enemigos en la pantalla.
            enemy.draw(screen)

    def add_enemy(self): #Elije a un enemigo aleatorio (Enemy_1 o Enemy_2), lo añade a la lista
        if len(self.enemies) < (self.enemy_count + 1): #Mientras mas enemigos sean eliminados, más apareceran
            enemy = random.choice([Enemy(ENEMY_1), Enemy(ENEMY_2)]) #Esto con el fin de añadir dificultad al juego
            self.enemies.append(enemy)

    def enemy_died(self): 
        self.enemy_count += 1
        #Cada vez que muere un enemigo se incrementa el contador. (Se explica en la linea 25)