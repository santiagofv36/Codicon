import pygame
from Global.constants import *
from Classes.player import Player
from pygame.locals import *
from Classes.webcam import Webcam
from Classes.enemy import Fire
from Classes.Objects import Objeto
from Global.events import *
from Classes.background import Background
import Global.globals as globals
import random
import pygame.mixer

import cv2
import mediapipe as mp
import math

'''
    Clase que representa el juego
'''

class Game:
    '''
        Inicializador de la clase
    '''
    def __init__(self):
        '''
            Se inicializan las variables necesarias para el juego
        '''
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        self.running = True
        self.started = False

        '''
            Se inicializan las variables necesarias para el uso de la webcam y la libreria Facemesh
        '''
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        '''
            Se inicializa el juego
        '''
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Boxxi")

        '''
            Se cargan las fuentes y el fondo
        '''

        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.smaller_font = pygame.font.Font('freesansbold.ttf', 22)
        self.super_small_font = pygame.font.Font('freesansbold.ttf', 16)
        self.background = Background()

        self.initialize()

    def initialize(self):
        '''
            Se define el estado inicial del juego
        '''
        
        self.start_time = pygame.time.get_ticks()
        self.last_frame_time = self.start_time
        self.player = Player()
        self.movement = 0

        '''
            Contadores para la creacion de enemigos y objetos
        '''
        self.enemy_timer = 500
        pygame.time.set_timer(ADD_ENEMY, self.enemy_timer)
        self.object_timer = 1000
        pygame.time.set_timer(ADD_OBJECT, self.object_timer)

        '''
            Se crean los grupos de enemigos y objetos
        '''
        self.enemies = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()

        self.lost = False
        self.score = 0

        '''
            Se inicializa la webcam
        '''

        self.webcam = Webcam().start()
        
        '''
            Se inicializan las variables necesarias para el calculo de la posicion de la cara    
        '''
        self.max_face_surf_height=0
        self.face_left_x = 0
        self.face_right_x = 0
        self.face_top_y = 0
        self.face_bottom_y = 0

        '''
            Se inicializa los efectos de sonido y musica de fondo
        '''
        pygame.mixer.music.load('sprites/Sounds/music.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()


        self.loose = pygame.mixer.Sound('sprites/Sounds/game_over.mp3')
        self.grab = pygame.mixer.Sound('sprites/Sounds/success.mp3')
        self.loose.set_volume(0.5)
        self.grab.set_volume(0.5)




    '''
        Funcion que se encarga de dibujar los elementos del juego
    '''

    def update(self, delta_time):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

        if self.lost or not self.started:
            for event in events:
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.initialize()
                    self.started = True
        else:
            '''
                Se aumenta la velocidad del juego a medida que pasa el tiempo
            '''
            globals.game_speed = 1 + ( (pygame.time.get_ticks() - self.start_time) / 1000) * .1
            # self.score = self.score + (delta_time * globals.game_speed)

            for event in events:
                '''
                    Generacion de enemigos
                '''
                if event.type == ADD_ENEMY:
                    num = random.randint(1,2)
                    for _ in range(num):
                        enemy = Fire()
                        self.enemies.add(enemy)
                    '''
                        Actualizar el timer que define cuando aparecera un nuevo enemigo
                    '''
                    self.enemy_timer = 500 - ((globals.game_speed - 1) * 100)
                    if self.enemy_timer < 50: self.enemy_timer = 50
                    pygame.time.set_timer(ADD_ENEMY, int(self.enemy_timer))
                
                '''
                    Generacion de objetos
                '''
                if event.type == ADD_OBJECT:
                    num = random.randint(1,2)
                    for _ in range(num):
                        object = Objeto()
                        self.objects.add(object)
                    '''
                        Actualizar el timer que define cuando aparecera un nuevo objeto
                    '''
                    self.object_timer = 1000 - ((globals.game_speed - 1) * 100)
                    if self.object_timer < 50: self.object_timer = 50
                    pygame.time.set_timer(ADD_OBJECT, int(self.object_timer))

            self.player.update(self.movement, delta_time)
            self.objects.update(delta_time)
            self.enemies.update(delta_time)
            self.process_collisions()
            self.background.update(delta_time)

    def process_collisions(self):
        '''
            Las colisiones se chequean con las mascaras de los sprites
        '''
        collide = pygame.sprite.spritecollide(self.player, self.enemies, False, pygame.sprite.collide_mask)
        # Chequeo si colisiono con algun enemigo
        if collide:
            self.loose.play()
            pygame.mixer.music.stop()
            self.lost = True

        #chequeo si colisiono con algun objeto para sumar puntos
        if grabObject := pygame.sprite.spritecollide(
            self.player, self.objects, True, pygame.sprite.collide_mask
        ):
            for obj in grabObject:
                self.grab.play()
                self.score += obj.score
                obj.kill()


    '''
        Funcion que se encarga de dibujar los elementos del juego
    '''
    def render(self):
        self.screen.fill((0,0,0))

        self.background.render(self.screen)

        '''
            Se dibuja la webcam
        '''

        if self.webcam.lastFrame is not None:
            self.render_camera()

        self.screen.blit(self.player.surf, self.player.rect)

        '''
            Se dibujan los enemigos y objetos
        '''

        for e in self.enemies:
            self.screen.blit(e.surf, e.rect)

        for o in self.objects:
            self.screen.blit(o.surf, o.rect)

        '''
            Se dibuja el puntaje
        '''

        display_score = self.score
        text_score = self.font.render(
            f'Score: {str(display_score)}', True, (255, 255, 255)
        )
        scoreTextRect = text_score.get_rect()
        scoreTextRect.bottom = SCREEN_HEIGHT-5
        scoreTextRect.left = 5
        self.screen.blit(text_score, scoreTextRect)

        '''
            Se dibuja el mensaje de game over
        '''

        if self.lost:
            self._Start_Restart_Game('Has Perdido!')
            retry_text = self.smaller_font.render('Presiona Enter para reintentar', True, (200,200,200), (0,0,0))
            retry_text_rect = retry_text.get_rect()
            retry_text_rect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 40)
            self.screen.blit(retry_text, retry_text_rect)

        '''
            Se dibuja el mensaje de inicio
        '''

        if not self.started:
            self._Start_Restart_Game('Presiona Enter para comenzar')
        pygame.display.flip()

    def _Start_Restart_Game(self, arg0):
        # titlo principal
        game_over_text = self.font.render(arg0, True, (255,255,255), (0,0,0))
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.screen.blit(game_over_text, game_over_text_rect)
        if arg0 == "Presiona Enter para comenzar":
            # instrucciones
            instructions_text = self.super_small_font.render('Inclina tu cara a los lados para moverte, recoge objetos para obtener puntos y evita los fuegos! Exito!', True, (200,200,200), (0,0,0))
            instructions_text_rect = instructions_text.get_rect()
            instructions_text_rect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 1.5) + 20)
            self.screen.blit(instructions_text, instructions_text_rect)



    def loop(self):
        with self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            min_detection_confidence=0.5,
            refine_landmarks=True
        ) as self.face_mesh:
            while self.running:
                if not self.lost:
                    if not self.webcam.ready():
                        continue
                    self.process_camera()

                time = pygame.time.get_ticks()
                delta_time = time - self.last_frame_time
                self.last_frame_time = time
                self.update(delta_time)
                self.render()
                self.clock.tick(60)
            pygame.quit()

    '''
        Funcion que se encarga de procesar la webcam
    '''

    def process_camera(self):
        image = self.webcam.read()
        if image is not None:
            image.flags.writeable = False
            image = cv2.flip(image, 1)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            results = self.face_mesh.process(image)
            self.webcam_image = image
            if results.multi_face_landmarks is not None:
                for face_landmarks in results.multi_face_landmarks:

                    '''
                        Se obtienen las coordenadas de los puntos de la cara
                    '''
                    top = (face_landmarks.landmark[10].x, face_landmarks.landmark[10].y)
                    bottom = (face_landmarks.landmark[152].x, face_landmarks.landmark[152].y)

                    #Obtener coordenadas del cuadrado de la cara
                    self.face_left_x = face_landmarks.landmark[234].x
                    self.face_right_x = face_landmarks.landmark[454].x
                    self.face_top_y = face_landmarks.landmark[10].y
                    self.face_bottom_y = face_landmarks.landmark[152].y

                    
                    self.face_left_x = self.face_left_x - .1
                    self.face_right_x = self.face_right_x + .1
                    self.face_top_y = self.face_top_y - .1
                    self.face_bottom_y = self.face_bottom_y + .1

                    cv2.line(
                        self.webcam_image, 
                        (int(top[0] * self.webcam.width()), int(top[1] * self.webcam.height())),
                        (int(bottom[0] * self.webcam.width()), int(bottom[1] * self.webcam.height())),
                        (0, 255, 0), 3
                    )

                    cv2.circle(self.webcam_image, (int(top[0] * self.webcam.width()), int(top[1] * self.webcam.height())), 8, (0,0,255), -1)
                    cv2.circle(self.webcam_image, (int(bottom[0] * self.webcam.width()), int(bottom[1] * self.webcam.height())), 8, (0,0,255), -1)

                    #Deteccion de angulo de la cara para moverse
                    self.detect_head_movement(top, bottom)

            k = cv2.waitKey(1) & 0xFF

    def detect_head_movement(self, top, bottom):
        radians = math.atan2(bottom[1] - top[1], bottom[0] - top[0])
        degrees = math.degrees(radians)

        #Angulo de deteccion de 70 a 110 (-1 a 1)
        min_degrees = 70
        max_degrees = 110
        degree_range = max_degrees - min_degrees

        degrees = max(degrees, min_degrees)
        degrees = min(degrees, max_degrees)

        self.movement = ( ((degrees-min_degrees) / degree_range) * 2) - 1

    def render_camera(self):        
        self.face_left_x = max(self.face_left_x, 0)
        self.face_right_x = min(self.face_right_x, 1)
        self.face_top_y = max(self.face_top_y, 0)
        self.face_bottom_y = min(self.face_bottom_y, 1)

        face_surf = pygame.image.frombuffer(self.webcam_image, (int(self.webcam.width()), int(self.webcam.height())), "BGR")

        face_rect = pygame.Rect(
            int(self.face_left_x*self.webcam.width()),
            int(self.face_top_y*self.webcam.height()), 
            int(self.face_right_x*self.webcam.width()) - int(self.face_left_x*self.webcam.width()),
            int(self.face_bottom_y*self.webcam.height()) - int(self.face_top_y*self.webcam.height())
        )

        only_face_surf = pygame.Surface((
            int(self.face_right_x*self.webcam.width()) - int(self.face_left_x*self.webcam.width()),
            int(self.face_bottom_y*self.webcam.height()) - int(self.face_top_y*self.webcam.height())
        ))
        only_face_surf.blit(face_surf, (0,0), face_rect)

        height = only_face_surf.get_rect().height
        width = only_face_surf.get_rect().width
        if width == 0:
            width = 1
        face_ratio =  height / width
        face_area_width = 130
        face_area_height = face_area_width * face_ratio
        if (face_area_height > self.max_face_surf_height):
            self.max_face_surf_height = face_area_height
        only_face_surf = pygame.transform.scale(
            only_face_surf, (face_area_width, int(self.max_face_surf_height))
        )
        self.screen.blit(only_face_surf, only_face_surf.get_rect())