from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy1 = Enemy(ENEMY_1)
            enemy2 = Enemy(ENEMY_2)
            self.enemies.append(enemy1)
            self.enemies.append(enemy2)