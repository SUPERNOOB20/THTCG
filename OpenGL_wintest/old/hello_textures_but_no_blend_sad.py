# Notes:
#    pip install pythonp2p




# import tkinter as tk    <--- NO
import pygame     # Imports pygame-ce

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


# youmu_card_raw = pygame.image.load("Youmu.png").convert()

youmu_card_raw = pygame.image.load(r"D:\OpenGL_wintest\Youmu.png").convert_alpha()
width, height = youmu_card_raw.size        # width = img.size. And also, height = img.size
youmu_card_data = pygame.image.tobytes(youmu_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture = glGenTextures(1)      # texture: np.uint32(1)


glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Texture binding.
glBindTexture(GL_TEXTURE_2D, texture)



# Texture parameter setting.
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)

glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0 , GL_RGBA, GL_UNSIGNED_BYTE, youmu_card_data)



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

    """
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.75, 0.0)
    glVertex2f(0.55, -0.1)
    glVertex2f(0.15, 0.3)
    glEnd()
    """


    """
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, 0.8) # top-left corner
    glVertex2f(0.5, 0.8) # top-right corner
    glVertex2f(0.5, -0.8) # bottom right corner
    glVertex2f(-0.5, -0.8) # bottom left corner
    glEnd()
    """


    # glBegin(GL_TRIANGLE_STRIP)

    glBegin(GL_POLYGON)
    
    glTexCoord2fv((0, 0))
    # glColor4f(1.0, 0.0, 0.0, 0.1)
    glVertex2f(-0.35, 0.8)
    glColor(1.0, 0.0, 0.0, 0.1)
    
    glTexCoord2fv((1, 0))
    # glColor4f(0.0, 1.0, 0.0, 0.1)
    glVertex2f(0.35, 0.8)
    glColor(0.0, 1.0, 0.0, 0.1)

    glTexCoord2fv((1, 1))
    # glColor4f(0.0, 0.0, 1.0, 0.1)
    glVertex2f(0.35, -0.8)
    glColor(0.0, 0.0, 1.0, 0.1)

    glTexCoord2fv((0, 1))
    # glColor4f(0.0, 0.0, 1.0, 0.1)
    glVertex2f(-0.35, -0.8)
    glColor(1.0, 1.0, 1.0, 0.1)

    glEnd()



    # Game code goes here



    # flip() the display to refresh the screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
import sys
sys.exit