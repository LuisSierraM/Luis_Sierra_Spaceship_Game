import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, ICON, FONT_STYLE
from game.components.spaceship	import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager

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
        self.power_up_manager = PowerUpManager()

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
        self.power_up_manager.update(self)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
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
            message =  f"Game Over\nYour Score: {self.score}\nHigh Score: {self.get_high_score()}\nTotal Deaths: {self.death_count}"
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
        #Se guarda la puntuación más alta en un archivo
        #llamado "high_score.txt" cada vez que el juego finaliza con una puntuación
        #mayor que la puntuación más alta previa. El archivo se crea si no existe
        #y se sobrescribe si ya existe.
        with open("high_score.txt", "w") as file: #With se utiliza para trabajar un recursos externos.
            file.write(str(score)) #Se asegura de cerrar estos recursos cuando ya no sean necesarios.

    def load_high_score(self):
        #Se carga la puntuación más alta desde el archivo
        #"high_score.txt". Lee el valor almacenado como
        #una cadena y lo convierte a un entero antes de devolverlo.
        try: #Lee el archivo y lo convierte a entero
            with open("high_score.txt", "r") as file:
                high_score = int(file.read())
        except FileNotFoundError: #Casos excepcionales
            high_score = 0
        return high_score
     
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                time_left_text = f"Time left: {time_to_show} seconds"
                font = pygame.font.Font(FONT_STYLE, 20)
                text_surface = font.render(time_left_text, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
                self.screen.blit(text_surface, text_rect)
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
    
    

