import pygame
from Global.constants import *
import random
import Global.globals as globals

ORIGINAL_SIZE=(60,154)
MIN_WIDTH = 25
MAX_WIDTH = 50

'''
    Clase que representa el fuego que cae del cielo
'''

class Fire(pygame.sprite.Sprite):
    
    '''
        Inicializador de la clase
    '''
    
    def __init__(self):
        super(Fire, self).__init__()

        
        '''
            Se escala el fuego para que se vea mas pequeño, de forma aleatoria con un maximo de 50 pixeles de ancho, los fuegos u obstaculos siempre son mas grandes que los objetos
        '''

        self.width = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.height = (self.width/ORIGINAL_SIZE[0])*ORIGINAL_SIZE[1]

        '''
            Se carga la imagen del fuego y se le aplica la escala
        '''

        self.surf = pygame.image.load('sprites/Fuego.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.width,self.height))
        self.mask = pygame.mask.from_surface(self.surf)

        '''
            Se crea el rectangulo que representa el fuego y se le asigna una posicion aleatoria en el eje x y una posicion aleatoria en el eje y que este fuera de la pantalla
        '''

        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(-100, -20)
            )
        )
        
        '''
            Velocidad semi-aleatoria, aumenta con la velocidad global del juego
        '''

        self.speed = (random.randint(1,2) / 10 ) * (1 + (globals.game_speed/2))

    '''
        Metodo que actualiza la posicion del fuego para simular la caida
    '''

    def update(self, delta_time):
        self.rect.move_ip(0, self.speed * delta_time)
        self.mask = pygame.mask.from_surface(self.surf)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()