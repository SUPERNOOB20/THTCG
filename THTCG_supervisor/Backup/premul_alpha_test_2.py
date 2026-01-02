import pygame

pygame.init()

pygame.display.set_caption("Premultiplied Alpha")
display_surf = pygame.display.set_mode((300, 170))

text_font = pygame.font.Font("Fonts/phosphor.ttf", size=12)




tool_tip_text = pygame.Surface((100, 100), flags=pygame.SRCALPHA)   # pill size: 488x182
tool_tip_text.fill((255, 255, 255, 85))
tool_tip_text = tool_tip_text.premul_alpha()

tool_tip_surf = pygame.Surface((120, 120), flags=pygame.SRCALPHA)
tool_tip_surf.fill((50, 50, 50, 255))
tool_tip_surf = tool_tip_surf.premul_alpha()

tool_tip_surf.blit(tool_tip_text, (10, 10), special_flags=pygame.BLEND_PREMULTIPLIED)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surf.fill((180, 140, 50))

    display_surf.blit(tool_tip_surf, (25, 25), special_flags=pygame.BLEND_PREMULTIPLIED)

    pygame.display.flip()