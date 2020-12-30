import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #class to manage bullets that ship fires

    def __init__(self, ai_settings, screen, ship):
        #create bullet at ships current location
        super(Bullet, self).__init__()
        self.screen = screen

        #create bullet at (0, 0) then set correct location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's location as a decimel
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #move bullet up screen
        #update decimal location
        self.y -= self.speed_factor
        #update rect location
        self.rect.y = self.y

    def draw_bullet(self):
        #draw bullet to screen
        pygame.draw.rect(self.screen, self.color, self.rect)