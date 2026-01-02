# Notes:
#    pip install pythonp2p




# import tkinter as tk    <--- NO
import pygame     # Imports pygame-ce
import deck_loader

from math import floor

from screeninfo import get_monitors
user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height


# Borrows the "viewport" concept from HTML for simplicity :)
vw: int = floor(user_screen_width / 100)
vh: int = floor(user_screen_height / 100)


import os

startup_directory = os.path.abspath(os.path.dirname(__file__))   # /.../THTCG

default_deck = deck_loader.load_deck(f"{startup_directory}/Decks/included_ingame/Default.csv")
full_deck = deck_loader.load_deck(f"{startup_directory}/Decks/included_ingame/Full.csv")

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

exit_game = False
is_on_fullscreen = True


if ((getattr(pygame, "IS_CE", False)) == 1):
    print("pygame-ce status: OK")
else:
    print("pygame-ce status: NOT CE")


title_screen_surf_raw = pygame.image.load('Graphics/title_screen.png').convert()
pill_surf_raw = pygame.image.load('Graphics/pill.png').convert_alpha()

title_screen_surf = pygame.transform.scale(surface = title_screen_surf_raw, size = (user_screen_width, user_screen_height))
pill_surf         = pygame.transform.scale(surface = pill_surf_raw,         size = (vw * 20, vh * 13))




# highlighted_pill_surf = pygame.Surface((500, 200), flags=pygame.SRCALPHA)   # pill size: 488x182
highlighted_pill_surf = pygame.Surface((vw * 20, vh * 13), flags=pygame.SRCALPHA)   # pill size: 488x182

highlighted_pill_surf.fill((255, 255, 255, 125))

highlighted_pill_surf = highlighted_pill_surf.premul_alpha()

pill_surf.blit(highlighted_pill_surf, (0, 0), special_flags=pygame.BLEND_PREMULTIPLIED)


clock = pygame.time.Clock()
running = True

while(running):
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE))):
            running = False
            
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Game code goes here

    screen.blit(title_screen_surf, (0, 0))
    screen.blit(pill_surf, (vw * 80, vh * 70))

    # flip() the display to refresh the screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
import sys
sys.exit