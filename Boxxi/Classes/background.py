import pygame
from Global.constants import *

'''
    Clase que representa el fondo del juego
'''

class Background(pygame.sprite.Sprite):
    
    '''
        Inicializador de la clase
    '''

    def __init__(self):
        super(Background, self).__init__()

        ''''
            Se carga la imagen del fondo y se le aplica la escalacion
        '''

        self.surf = pygame.image.load("sprites/Fondo.png")
        background_width = SCREEN_WIDTH * 2 
        background_height = (background_width/self.surf.get_width())*self.surf.get_height()
        self.surf = pygame.transform.scale(self.surf, (background_width, background_height))
        
        '''
            Se crean dos rectangulos que representan el fondo, uno se ubica debajo del otro para simular un scroll infinito
        '''

        self.rect = self.surf.get_rect(
            bottomleft=(0,SCREEN_HEIGHT)
        )
        self.surf2 = self.surf
        self.rect2 = self.surf2.get_rect(
            bottomleft=self.rect.topleft
        )
        self.ypos = 0
        self.ypos2 = background_height-SCREEN_HEIGHT
    
    '''
        Simulacion de un scroll infinito
    '''

    def update(self, delta_time):
        self.ypos += .05 * delta_time
        self.ypos2 += .05 * delta_time
        self.rect.y = int(self.ypos)
        self.rect2.y = int(self.ypos2)
        if self.rect.y > SCREEN_HEIGHT:
            self.ypos = self.rect2.y - self.surf2.get_height()
            self.rect.y = self.ypos
        if self.rect2.y > SCREEN_HEIGHT:
            self.ypos2 = self.rect.y - self.surf.get_height()
            self.rect2.y = self.ypos2

    '''
        Renderiza el fondo
    '''

    def render(self, dest):
        dest.blit(self.surf, self.rect)
        dest.blit(self.surf2, self.rect2)