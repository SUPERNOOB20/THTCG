# Notes:
#    pip install pythonp2p




# import tkinter as tk    <--- NO
import pygame     # Imports pygame-ce
from rgba_to_floating_point import *


from OpenGL.GL import *
# from OpenGL.GLU import *


from math import floor, ceil

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
width, height = youmu_card_raw.size        # width = img.size. And also, height = img.size
youmu_card_data = pygame.image.tobytes(youmu_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture1 = glGenTextures(1)      # texture: np.uint32(1)


# WILL FIX LATER
remi_card_raw = pygame.image.load(r"D:\SUPERNOOB_Studios\Indie_Development\Games\Python\THTCG\OpenGL_wintest\Remi.png").convert_alpha()
width, height = youmu_card_raw.size        # width = img.size. And also, height = img.size
youmu_card_data = pygame.image.tobytes(youmu_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture2 = glGenTextures(2)      # texture: np.uint32(1)


# WILL FIX LATER
ascent_card_raw = pygame.image.load(r"D:\SUPERNOOB_Studios\Indie_Development\Games\Python\THTCG\OpenGL_wintest\Ascent.png").convert_alpha()
width, height = youmu_card_raw.size        # width = img.size. And also, height = img.size
ascent_card_data = pygame.image.tobytes(youmu_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture3 = glGenTextures(3)      # texture: np.uint32(1)



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






def draw_card(ID: str, color: str, x: float, y: float, width: float, height: float):
    

    # Texture binding.
    # TODO: Improve this code x-x
    match ID:
        case 1:
            glBindTexture(GL_TEXTURE_2D, texture1)
        case 2:
            glBindTexture(GL_TEXTURE_2D, texture2)
        case 3:
            glBindTexture(GL_TEXTURE_2D, texture3)



    # Texture parameter setting.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0 , GL_RGBA, GL_UNSIGNED_BYTE, youmu_card_data)

    # glEnable(GL_BLEND)



    shader_colors = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]        # initializes shader_colors

    match color:
        case "red":
            shader_colors = [[0.3, 0.0, 0.0], [0.8, 0.0, 0.0]]    # Colours for bottom-left and top-right corners, respectively :3
        case "yellow":
            shader_colors = [[0.3, 0.3, 0.0], [0.8, 0.8, 0.0]]
        case "blue":
            shader_colors = [[0.0, 0.0, 0.3], [0.0, 0.0, 0.8]]
        case _:
            i = 0   # nop instruction



    x_0 = (ceil(x/50)) - 1
    y_0 = (ceil(y/50)) - 1

    x_1 = x_0 + (ceil(width/50)) - 1
    y_1 = y_0 + (ceil(height/50)) - 1

    glBegin(GL_POLYGON)


    # TOP-LEFT CORNER OF THE CARD
    glColor4f(1, 1, 1, 1.0)    
    # glBlendColor(1.0, 0.0, 0.0, 0.1)    
    glTexCoord2fv((0, 0))
    glVertex2f(x_0, y_0)
    
    # TOP-RIGHT CORNER OF THE CARD
    glColor4f(shader_colors[0][0], shader_colors[0][1], shader_colors[0][2], 1.0)
    # glBlendColor(0.0, 1.0, 0.0, 0.1)
    glTexCoord2fv((1, 0))
    glVertex2f(x_1, y_0)

    # BOTTOM-RIGHT CORNER OF THE CARD
    # glColor4f(0.1, 0.1, 1.0, 1.0)
    # glBlendColor(0.0, 0.0, 1.0, 0.1)
    glTexCoord2fv((1, 1))
    glVertex2f(x_1, y_1)


    # BOTTOM-LEFT CORNER OF THE CARD
    glColor4f(shader_colors[1][0], shader_colors[1][1], shader_colors[1][2], 1.0)
    # glBlendColor(1.0, 1.0, 1.0, 0.1)
    glTexCoord2fv((0, 1))
    glVertex2f(x_0, y_1)
    

    glEnd()


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


    draw_card('youmu', "blue", 10, 10, 20, 80)
    draw_card('remi', "red", 40, 40, 20, 80)
    draw_card('ascent', "yellow", 70, 70, 20, 80)
    


    # Game code goes here









    # flip() the display to refresh the screen
    pygame.display.flip()

    # clock.tick(60)  # limits FPS to 60
    clock.tick()

    framerate = int(clock.get_fps())
    pygame.display.set_caption(f"FPS: {framerate}")

pygame.quit()
import sys
sys.exit