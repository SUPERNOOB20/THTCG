# Notes:
#    pip install pythonp2p




# import tkinter as tk    <--- NO
import pygame     # Imports pygame-ce
from rgba_to_floating_point import *


from OpenGL.GL import *
# from OpenGL.GLU import *


from math import floor

from screeninfo import get_monitors
user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height


# Borrows the "viewport" concept from HTML for simplicity :)
vw: int = floor(user_screen_width / 100)
vh: int = floor(user_screen_height / 100)


import os

startup_directory = os.path.abspath(os.path.dirname(__file__))   # /.../THTCG


pygame.init()
pygame.font.init()
# screen = pygame.display.set_mode((0, 0), pygame.DOUBLEBUF | pygame.OPENGL)
screen = pygame.display.set_mode((1280, 720), pygame.DOUBLEBUF | pygame.OPENGL)

GREEN = (0, 90, 0)
glClearColor(0.9, 0.6, 0.9, 1.0)

# coloured_screen = pygame.Surface()

exit_game = False
is_on_fullscreen = True


if ((getattr(pygame, "IS_CE", False)) == 1):
    print("pygame-ce status: OK")
else:
    print("pygame-ce status: NOT CE")


clock = pygame.time.Clock()
running = True

glEnable(GL_TEXTURE_2D)        # legacy OpenGL feature?
glEnable(GL_BLEND)

# youmu_card_raw = pygame.image.load("Youmu.png").convert()

# WILL FIX LATER
youmu_card_raw = pygame.image.load(r"D:\SUPERNOOB_Studios\Indie_Development\Games\Python\THTCG\OpenGL_wintest\Youmu.png").convert_alpha()
youmu_card_smol = pygame.transform.scale(surface = youmu_card_raw, size = (250, 500))
youmu_width, youmu_height = youmu_card_smol.size     # NO IDEA how this works.
youmu_card_data = pygame.image.tobytes(youmu_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture1 = glGenTextures(1)      # texture: np.uint32(1)


# WILL FIX LATER
remi_card_raw = pygame.image.load(r"D:\SUPERNOOB_Studios\Indie_Development\Games\Python\THTCG\OpenGL_wintest\Remi.png").convert_alpha()
remi_card_smol = pygame.transform.scale(surface = remi_card_raw, size = (250, 500))
remi_width, remi_height = remi_card_smol.size        # NO IDEA how this works.
remi_card_data = pygame.image.tobytes(remi_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture2 = glGenTextures(1)      # texture: np.uint32(1)


# WILL FIX LATER
ascent_card_raw = pygame.image.load(r"D:\SUPERNOOB_Studios\Indie_Development\Games\Python\THTCG\OpenGL_wintest\Ascent.png").convert_alpha()
ascent_card_smol = pygame.transform.scale(surface = ascent_card_raw, size = (250, 500))
ascent_width, ascent_height = ascent_card_smol.size      # NO IDEA how this works.
ascent_card_data = pygame.image.tobytes(ascent_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture3 = glGenTextures(1)      # texture: np.uint32(1)



# glBlendFunc(GL_ONE_MINUS_SRC_ALPHA, GL_SRC_ALPHA)
# glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_DST_COLOR)

# glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_COLOR)

# glBlendFunc(GL_SRC_ALPHA, GL_ONE)

# glBlendFunc(GL_SRC_ALPHA, GL_ZERO)




# glBlendFunc(GL_ONE, GL_ONE_MINUS_DST_COLOR)
# glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA)
# glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_COLOR)
# glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_COLOR)

glBlendFunc(GL_ONE, GL_CONSTANT_COLOR)


# glBlendFunc(GL_ONE, GL_ONE)





# glBlendEquation(GL_MIN)



frame_counter: int = 0


def draw_card(ID: str, color: str, x: float, y: float, card_width: float, card_height: float):
    
    width = 0
    height = 0
    card_data = 0

    # Texture binding.
    # TODO: Improve this code x-x
    match ID:
        case "youmu":
            glBindTexture(GL_TEXTURE_2D, texture1)
            width = youmu_width
            height = youmu_height
            card_data = youmu_card_data
        case "remi":
            glBindTexture(GL_TEXTURE_2D, texture2)
            width = remi_width
            height = remi_height
            card_data = remi_card_data
        case "ascent":
            glBindTexture(GL_TEXTURE_2D, texture3)
            width = ascent_width
            height = ascent_height
            card_data = ascent_card_data
        case _:
            j = 0 # nop instruction



    # Texture parameter setting.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0 , GL_RGBA, GL_UNSIGNED_BYTE, card_data)

    # glEnable(GL_BLEND)



    shader_colors = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]        # initializes shader_colors

    match color:
        case "red":
            shader_colors = [[0.8, 0.0, 0.0], [0.7, 0.4, 0.4]]    # Colours for top-right and bottom left corners, respectively :3
        case "yellow":
            shader_colors = [[0.8, 0.8, 0.0], [0.7, 0.7, 0.4]]
        case "blue":
            shader_colors = [[0.0, 0.0, 0.8], [0.4, 0.4, 0.7]]
        case _:
            i = 0   # nop instruction



    x_0 = (x/50) - 1
    y_0 = (y/50) - 1

    x_1 = x_0 + (card_width/50)
    y_1 = y_0 + (card_height/50)




    glBegin(GL_POLYGON)


    # TOP-LEFT CORNER OF THE CARD
    glColor4f(1.0, 1.0, 1.0, 1.0)    
    # glBlendColor(1.0, 0.0, 0.0, 0.1)    
    glTexCoord2fv((0, 0))
    glVertex2f(x_0, y_0)
    
    # TOP-RIGHT CORNER OF THE CARD
    glColor4f(shader_colors[0][0], shader_colors[0][1], shader_colors[0][2], 1.0)
    # glBlendColor(0.0, 1.0, 0.0, 0.1)
    glTexCoord2fv((1, 0))
    glVertex2f(x_1, y_0)

    # BOTTOM-RIGHT CORNER OF THE CARD
    glColor4f(1.0, 1.0, 1.0, 1.0)
    # glBlendColor(0.0, 0.0, 1.0, 0.1)
    glTexCoord2fv((1, 1))
    glVertex2f(x_1, y_1)


    # BOTTOM-LEFT CORNER OF THE CARD
    glColor4f(shader_colors[1][0], shader_colors[1][1], shader_colors[1][2], 1.0)
    # glBlendColor(1.0, 1.0, 1.0, 0.1)
    glTexCoord2fv((0, 1))
    glVertex2f(x_0, y_1)
    

    glEnd()

    # glTranslatef(width, 0, 0)
    # glScalef(-1,1,1)

    # if (frame_counter % 2000 == 0):
        # glTranslatef(width, 0, 0)
        # glScalef(-1,1,1)

    return





title_screen_menu: int = 1
deck_is_loaded: bool = False

while(running):
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE))):
            running = False
        

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill(GREEN)

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(32)

    # glBegin(GL_POLYGON)

    draw_card('youmu', "blue", 10.0, 10.0, 20.0, 80.0)
    draw_card('remi', "red", 40.0, 10.0, 20.0, 80.0)
    draw_card('ascent', "yellow", 70.0, 10.0, 20.0, 80.0)
    
    # glEnd()

    # Game code goes here





    frame_counter += 1



    # flip() the display to refresh the screen
    pygame.display.flip()

    # clock.tick(60)  # limits FPS to 60
    clock.tick()  # unlimited FPS :O

    framerate = int(clock.get_fps())
    pygame.display.set_caption(f"FPS: {framerate}")

pygame.quit()
import sys
sys.exit