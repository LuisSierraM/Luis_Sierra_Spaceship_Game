import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    def __init__(self, screen):
        screen.fill((255, 255, 255)) #Se ajusta color de la pantalla
        self.font = pygame.font.Font(FONT_STYLE, 30) #Se ajusta tamaño y fuente de letra
        self.messages = [] #Lista vacia de mensajes

    def update(self, game):
        pygame.display.update() #Se llama al metodo handle_events_on_menu
        self.handle_events_on_menu(game)

    def draw(self, screen):
        y_position = SCREEN_HEIGHT // 2 - 50 #Posicion vertical
        for message in self.messages:#A cada mensaje se le va asignar lo siguiente
            text = self.font.render(message, True, (0, 0, 0)) #Se ajusta color
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_position))#Se ajusta posicion
            screen.blit(text, text_rect)
            y_position += 30 #Diferencia de espacio entre cada mensaje

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN: #Por cualquier tecla que se presione se llama al metodo run
                game.run()

    def reset_screen_color (self, screen):
        screen.fill((255, 255, 255)) #La pantalla vuelve a su color normal

    def update_message(self, messages):
        self.messages = messages #Se actualiza la lista de los mensajes
