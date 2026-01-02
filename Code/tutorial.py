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
youmu_card_raw = pygame.image.load(f"{startup_directory}/Youmu.png").convert_alpha()
youmu_card_smol = pygame.transform.scale(surface = youmu_card_raw, size = (15*vw, 30*vh))
youmu_width, youmu_height = youmu_card_smol.size     # NO IDEA how this works.
youmu_card_data = pygame.image.tobytes(youmu_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture1 = glGenTextures(1)      # texture: np.uint32(1)


# WILL FIX LATER
remi_card_raw = pygame.image.load(f"{startup_directory}/Remi.png").convert_alpha()
remi_card_smol = pygame.transform.scale(surface = remi_card_raw, size = (15*vw, 30*vh))
remi_width, remi_height = remi_card_smol.size        # NO IDEA how this works.
remi_card_data = pygame.image.tobytes(remi_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture2 = glGenTextures(1)      # texture: np.uint32(1)


# WILL FIX LATER
ascent_card_raw = pygame.image.load(f"{startup_directory}/Ascent.png").convert_alpha()
ascent_card_smol = pygame.transform.scale(surface = ascent_card_raw, size = (15*vw, 30*vh))
ascent_width, ascent_height = ascent_card_smol.size      # NO IDEA how this works.
ascent_card_data = pygame.image.tobytes(ascent_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture3 = glGenTextures(1)      # texture: np.uint32(1)


yorihime_card_raw = pygame.image.load(f"{startup_directory}/Yorihime.png").convert_alpha()
yorihime_card_smol = pygame.transform.scale(surface = yorihime_card_raw, size = (15*vw, 30*vh))
yorihime_width, yorihime_height = yorihime_card_smol.size     # NO IDEA how this works.
yorihime_card_data = pygame.image.tobytes(yorihime_card_raw, "RGBA")      # image.tobytes() allows OpenGL to "understand" this data (to load the image).
texture4 = glGenTextures(1)      # texture: np.uint32(1)




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


def draw_card(ID: str, x: float, y: float, card_width: float, card_height: float):
    
    width = 0
    height = 0
    card_data = 0

    color = ""

    # Texture binding.
    # TODO: Improve this code x-x
    match ID:
        case "ascent":
            glBindTexture(GL_TEXTURE_2D, texture1)
            width = ascent_width
            height = ascent_height
            card_data = ascent_card_data
            color = "yellow"
        case "descent":
            glBindTexture(GL_TEXTURE_2D, texture2)
            width = descent_width
            height = descent_height
            card_data = descent_card_data
            color = "yellow"
        case "seija":
            glBindTexture(GL_TEXTURE_2D, texture3)
            width = seija_width
            height = seija_height
            card_data = seija_card_data
            color = "yellow"
        case "chimata":
            glBindTexture(GL_TEXTURE_2D, texture4)
            width = chimata_width
            height = chimata_height
            card_data = chimata_card_data
            color = "yellow"
        case "kosuzu":
            glBindTexture(GL_TEXTURE_2D, texture5)
            width = kosuzu_width
            height = kosuzu_height
            card_data = kosuzu_card_data
            color = "yellow"
        case "nazrin":
            glBindTexture(GL_TEXTURE_2D, texture6)
            width = nazrin_width
            height = nazrin_height
            card_data = nazrin_card_data
            color = "yellow"
        case "reimu":
            glBindTexture(GL_TEXTURE_2D, texture7)
            width = reimu_width
            height = reimu_height
            card_data = reimu_card_data
            color = "blue"
        case "okuu":
            glBindTexture(GL_TEXTURE_2D, texture8)
            width = okuu_width
            height = okuu_height
            card_data = okuu_card_data
            color = "red"
        case "kyouko":
            glBindTexture(GL_TEXTURE_2D, texture9)
            width = kyouko_width
            height = kyouko_height
            card_data = kyouko_card_data
            color = "blue"
        case "tenshi":
            glBindTexture(GL_TEXTURE_2D, texture10)
            width = tenshi_width
            height = tenshi_height
            card_data = tenshi_card_data
            color = "red"
        case "cirno":
            glBindTexture(GL_TEXTURE_2D, texture11)
            width = tenshi_width
            height = tenshi_height
            card_data = tenshi_card_data
            color = "blue"
        case "aya":
            glBindTexture(GL_TEXTURE_2D, texture12)
            width = tenshi_width
            height = tenshi_height
            card_data = tenshi_card_data
            color = "blue"
        case "keine":
            glBindTexture(GL_TEXTURE_2D, texture13)
            width = keine_width
            height = keine_height
            card_data = keine_card_data
            color = "blue"
        case "mystia":
            glBindTexture(GL_TEXTURE_2D, texture14)
            width = mystia_width
            height = mystia_height
            card_data = mystia_card_data
            color = "red"
        case "remilia":
            glBindTexture(GL_TEXTURE_2D, texture15)
            width = remilia_width
            height = remilia_height
            card_data = remilia_card_data
            color = "red"
        case "flandre":
            glBindTexture(GL_TEXTURE_2D, texture16)
            width = flandre_width
            height = flandre_height
            card_data = flandre_card_data
            color = "red"
        case "sakuya":
            glBindTexture(GL_TEXTURE_2D, texture17)
            width = sakuya_width
            height = sakuya_height
            card_data = sakuya_card_data
            color = "blue"
        case "wriggle":
            glBindTexture(GL_TEXTURE_2D, texture18)
            width = wriggle_width
            height = wriggle_height
            card_data = wriggle_card_data
            color = "red"
        case "youmu":
            glBindTexture(GL_TEXTURE_2D, texture19)
            width = youmu_width
            height = youmu_height
            card_data = youmu_card_data
            color = "blue"
        case "yuyuko":
            glBindTexture(GL_TEXTURE_2D, texture20)
            width = yuyuko_width
            height = yuyuko_height
            card_data = yuyuko_card_data
            color = "blue"
        case "seiga":
            glBindTexture(GL_TEXTURE_2D, texture21)
            width = seiga_width
            height = seiga_height
            card_data = seiga_card_data
            color = "red"
        case "yoshika":
            glBindTexture(GL_TEXTURE_2D, texture22)
            width = yoshika_width
            height = yoshika_height
            card_data = yoshika_card_data
            color = "red"
        case "momoyo":
            glBindTexture(GL_TEXTURE_2D, texture23)
            width = momoyo_width
            height = momoyo_height
            card_data = momoyo_card_data
            color = "red"
        case "meiling":
            glBindTexture(GL_TEXTURE_2D, texture24)
            width = meiling_width
            height = meiling_height
            card_data = meiling_card_data
            color = "blue"
        case "sanae":
            glBindTexture(GL_TEXTURE_2D, texture25)
            width = sanae_width
            height = sanae_height
            card_data = sanae_card_data
            color = "blue"
        case "patchouli":
            glBindTexture(GL_TEXTURE_2D, texture26)
            width = patchouli_width
            height = patchouli_height
            card_data = patchouli_card_data
            color = "red"
        case "yorihime":
            glBindTexture(GL_TEXTURE_2D, texture27)
            width = yorihime_width
            height = yorihime_height
            card_data = yorihime_card_data
            color = "blue"
        case "hijiri":
            glBindTexture(GL_TEXTURE_2D, texture28)
            width = hijiri_width
            height = hijiri_height
            card_data = hijiri_card_data
            color = "blue"

        case "yorihime":
            glBindTexture(GL_TEXTURE_2D, texture27)
            width = yorihime_width
            height = yorihime_height
            card_data = yorihime_card_data

        case _:
            print("ERROR: Invalid card ID [errorcode 1]")



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
            shader_colors = [[0.8, 0.3, 0.3], [0.7, 0.4, 0.4]]    # Colours for bottom-right and top-left corners, respectively :3
        case "yellow":
            shader_colors = [[0.8, 0.8, 0.5], [0.7, 0.7, 0.4]]
        case "blue":
            shader_colors = [[0.45, 0.45, 0.8], [0.8, 0.8, 1]]
        case _:
            print("ERROR: Invalid colour [errorcode 2].")  # nop instruction



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