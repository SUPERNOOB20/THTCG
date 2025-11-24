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
glClearColor(0.8, 0.1, 0.8, 1.0)

# coloured_screen = pygame.Surface()

exit_game = False
is_on_fullscreen = True


if ((getattr(pygame, "IS_CE", False)) == 1):
    print("pygame-ce status: OK")
else:
    print("pygame-ce status: NOT CE")


clock = pygame.time.Clock()
running = True



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


    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.65, -0.9)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.55, -0.7)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.25, 0.8)
    glEnd()



    # Game code goes here



    # flip() the display to refresh the screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
import sys
sys.exit