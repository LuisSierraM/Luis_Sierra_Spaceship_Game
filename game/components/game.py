import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, ICON, FONT_STYLE
from game.components.spaceship	import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.player_bullets = []
        self.running = False
        self.menu = Menu("Press Any Key To Start...", self.screen)
        self.score = 0
        self.death_count = 0
        self.high_score = self.load_high_score()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
        high_score = self.get_high_score()
        if self.score > high_score:
            self.high_score = self.score
            self.save_high_score(self.high_score)

    def save_high_score(self, score):
        self.high_score = score

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        self.menu.draw(self.screen)
        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            message =  f"Game Over\n\nYour Score: {self.score}\nHigh Score: {self.get_high_score()}\nTotal Deaths: {self.death_count}"
            self.menu.update_message(message)
            
        icon = self.image = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon, ((SCREEN_WIDTH // 2) -40, (SCREEN_HEIGHT // 2) - 150))

        self.menu.update(self)

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def get_high_score(self):
        return self.high_score
    
    def save_high_score(self, score):
        #Esta función se utiliza para guardar la puntuación más alta en un archivo
        #llamado "high_score.txt" cada vez que el juego finaliza con una puntuación
        #mayor que la puntuación más alta previa. El archivo se crea si no existe
        #y se sobrescribe si ya existe. Esto asegura que la puntuación más alta
        #persista entre ejecuciones del juego.
        with open("high_score.txt", "w") as file:
            file.write(str(score))

    def load_high_score(self):
        #Esta función se utiliza para cargar la puntuación más alta desde el archivo
        #"high_score.txt". Si el archivo no existe, se devuelve el valor predeterminado,
        #que es 0 en este caso. Si el archivo existe, lee el valor almacenado como
        #una cadena y lo convierte a un entero antes de devolverlo. Esto permite
        #mantener el valor del high score entre ejecuciones del juego.
        try:
            with open("high_score.txt", "r") as file:
                high_score = int(file.read())
        except FileNotFoundError:
            high_score = 0
        return high_score
    

