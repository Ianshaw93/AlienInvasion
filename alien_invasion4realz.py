import sys

import pygame

#group is a list

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien

import game_functions as gf

def run_game():
    # Initalise game and create screen object
    pygame.init()
    #ai = an instance
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    #make a ship
    ship = Ship(ai_settings, screen)
    #make a group to store bullets in; outside of main loop so not remade each iteration
    bullets = Group()
    # make a group to store aliens
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            # update bullets before aliens to allow aliens to disappear if hit
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()