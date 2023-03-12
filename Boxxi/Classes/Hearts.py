import pygame

class Hearts(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super(Hearts, self).__init__()
        self.surf = pygame.image.load("sprites/Heart.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (width, height))
        self.rect = self.surf.get_rect(
            center=(
                x,
                y
            )
        )

    def render(self, screen):
        screen.blit(self.surf, self.rect)
        
    