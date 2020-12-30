import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #class to show a single alien in fleet

    def __init__(self, ai_settings, screen):
        # initialise alien and give starting location
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set the rect coordinates
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect()

        # start each new alien top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's location
        self.x = float(self.rect.x)

    def blitme(self):
        #draw alien at current location
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        # return true if alien at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

    def update(self):
        # move alien to the right or left
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
