import pygame
from Global.constants import *
import random
import Global.globals as globals

MIN_WIDTH = 35
MAX_WIDTH = 50

Objects = [
    {
        'image': 'sprites/Billetes.png',
        'score': 50,
        'width': 260,
        'height': 243,
    } ,
    {
        'image': 'sprites/Oso.png',
        'score': 5,
        'width': 162,
        'height': 180,
    },
    {
        'image': 'sprites/Patito.png',
        'score': 10,
        'width': 254,
        'height': 251,
    },
    {
        'image': 'sprites/Pelota.png',
        'score': 15,
        'width': 232,
        'height': 217,
    },
    {
        'image': 'sprites/Regla.png',
        'score': 20,
        'width': 405,
        'height': 192,
    },
    {
        'image': 'sprites/Tren.png',
        'score': 25,
        'width': 311,
        'height': 207,
    },
]


class Objeto(pygame.sprite.Sprite):
    def __init__(self):
        super(Objeto, self).__init__()

        objeto = random.choice(Objects)

        #Tamano aleatorio
        self.width = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.height = (self.width/objeto['width'])*objeto['height']

        self.score = objeto['score']
        self.image = objeto['image']

        self.surf = pygame.image.load(self.image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.width,self.height))
        self.mask = pygame.mask.from_surface(self.surf)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(-100, -20)
            )
        )
        
        #Velocidad semi-aleatoria, aumenta con la velocidad global del juego
        self.speed = (random.randint(1,2) / 10 ) * (1 + (globals.game_speed/2))

    def update(self, delta_time):
        self.rect.move_ip(0, self.speed * delta_time)
        self.mask = pygame.mask.from_surface(self.surf)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()