# Notes:
#    pip install pythonp2p




# import tkinter as tk    <--- NO
import pygame     # Imports pygame-ce
import copy
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

dummy_surf                   = pygame.image.load('Graphics/dummy_test.png').convert_alpha()
title_screen_surf_raw        = pygame.image.load('Graphics/title_screen.png').convert()
pill_with_highlight_surf_raw = pygame.image.load('Graphics/pill.png').convert_alpha()
pill_highlight_raw           = pygame.image.load('Graphics/pill_highlight.png').convert_alpha()
deck_surf_raw                = pygame.image.load('Graphics/face_down_deck.png').convert_alpha()
black_pilled_surf_raw        = pygame.image.load('Graphics/black_pill.png').convert_alpha()
# pill_highlight_raw = pygame.image.load('Graphics/pill_highlight_full_opacity.png').convert_alpha()

title_screen_surf            = pygame.transform.scale(surface = title_screen_surf_raw,                size = (user_screen_width, user_screen_height))
pill_surf                    = pygame.transform.scale(surface = pill_with_highlight_surf_raw,         size = (vw * 20, vh * 13))
pill_with_highlight_surf     = pygame.transform.scale(surface = pill_with_highlight_surf_raw,         size = (vw * 20, vh * 13))
pill_highlight               = pygame.transform.scale(surface = pill_highlight_raw,                   size = (vw * 20, vh * 13))
deck_surf                    = pygame.transform.scale(surface = deck_surf_raw,                        size = (floor(vh * 18.83333), vh * 30))
black_pilled_surf            = pygame.transform.scale(surface = black_pilled_surf_raw,                size = (floor(user_screen_width / 2), floor(user_screen_height / 2)))




pill_highlighter = pygame.Surface((vw * 20, vh * 13), flags=pygame.SRCALPHA)   # pill size: 488x182

pill_highlighter = pill_highlighter.premul_alpha()

pill_highlighter.blit(pill_highlight, (0, 0), special_flags=pygame.BLEND_PREMULTIPLIED)
# pill_highlighter.blit(pill_highlight, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

pill_highlighter = pill_highlighter.premul_alpha()

# no_highlight_pill_with_highlight_surf = pill_with_highlight_surf.copy.deepcopy()

# pill_with_highlight_surf.blit(pill_highlighter, (0, 0), special_flags=pygame.BLEND_PREMULTIPLIED)
pill_with_highlight_surf.blit(pill_highlighter, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

clock = pygame.time.Clock()
running = True











title_screen_menu: int = 1

class Pill(pygame.sprite.Sprite):
    def __init__(self, menu_ID, pill_ID, width, height):
        super().__init__()

        # self.animation_index = 0
        self.image = pill_with_highlight_surf.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (width, height)


pill_hitbox_1a = Pill(1, 1, (vw * 85), (vh * 70))
pill_hitbox_1b = Pill(1, 2, (vw * 85), (vh * 85))
pill_hitbox_2a = Pill(2, 3, (vw * 85), (vh * 40))
pill_hitbox_2b = Pill(2, 4, (vw * 85), (vh * 52))
pill_hitbox_2c = Pill(2, 5, (vw * 85), (vh * 64))
pill_hitbox_2d = Pill(2, 6, (vw * 85), (vh * 76))
pill_hitbox_2e = Pill(2, 7, (vw * 85), (vh * 88))

pills_panel_1 = pygame.sprite.Group()
pills_panel_2 = pygame.sprite.Group()

pills_panel_1.add(pill_hitbox_1a)
pills_panel_1.add(pill_hitbox_1b)
pills_panel_2.add(pill_hitbox_2a)
pills_panel_2.add(pill_hitbox_2b)
pills_panel_2.add(pill_hitbox_2c)
pills_panel_2.add(pill_hitbox_2d)
pills_panel_2.add(pill_hitbox_2e)




class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = dummy_surf
        self.rect = self.image.get_rect()
        self.rect.topleft = pygame.mouse.get_pos()
        """
        mouse_pos = pygame.mouse.get_pos()
        self.rect = (0, 0)     # initializes self.rect with a dummy value.
        self.rect.center = mouse_pos
        """


mouse = pygame.sprite.GroupSingle()
mouse.add(Mouse())




def collision_sprite(menu_ID):

    match menu_ID:
        case 1:
            if (pygame.sprite.spritecollide(mouse.sprite, pills_panel_1, False)):
                return True
        
        case 2:
            if (pygame.sprite.spritecollide(mouse.sprite, pills_panel_2, False)):
                return True
            
        case _:
            return False







while(running):
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE))):
            running = False
        
        if collision_sprite(title_screen_menu):

            # trigger hover animation here.

            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):  # if player is clicking.
                title_screen_menu += 1
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Game code goes here


    screen.blit(title_screen_surf, (0, 0))
    
    match title_screen_menu:
        case 1:
            pills_panel_1.draw(screen)
        

        case 2:
            pills_panel_2.draw(screen)
        

        case 3:
            # render text and pill box to choose deck here

            black_pill_coords = black_pilled_surf.get_rect(center = (floor(user_screen_width / 2), floor((user_screen_height / 2) + vh * 10)))
            deck_surf_coords = deck_surf.get_rect(center = (floor(user_screen_width / 2), floor((user_screen_height / 2) + vh * 10)))

            black_pilled_surf.set_alpha(90)
            screen.blit(black_pilled_surf, black_pill_coords)

            screen.blit(deck_surf, deck_surf_coords)

            

        case _:
            pass
    

    # if mouse_pos_rect

    # screen.blit(pill_with_highlight_surf, (vw * 80, vh * 70))
    # screen.blit(pill_with_highlight_surf, (vw * 80, vh * 85))




    # screen.blit(pill_highlighter, (0, 0))
    # screen.blit(pill_surf, (0, 150))
    # screen.blit(pill_with_highlight_surf, (0, 300))


    # dummy_surf.get_rect(center = pygame.mouse.get_pos())

    # mouse.update()
    mouse = pygame.sprite.GroupSingle()
    mouse.add(Mouse())

    # flip() the display to refresh the screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
import sys
sys.exit