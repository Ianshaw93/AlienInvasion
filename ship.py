import pygame

class Ship():

    def __init__(self, ai_settings, screen):
    #initialise ship and set starting position
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship and retrieve its shape/rect: treated as rectangle
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each ship at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store decimal value for ship's centre
        self.center = float(self.rect.centerx)

        # movement flag or toggle
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update ship location dependent on movement toggle
        # two separate if statements so no prority given to moving right if both directional arrows pressed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect centre from self center
        self.rect.centerx = self.center

    def blitme(self):
        #blit = draw; ship at current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #center the ship on the screen
        self.center = self.screen_rect.centerx