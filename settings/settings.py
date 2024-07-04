import pygame

pygame.init()

map1 = [
    '                                                                ',
    '                                                                ',
    '           KEEL                                                 ',
    '          KTCCUL                                                ',
    '         KTCCCCUL                                               ',
    'EEEEEEEEETCCCCCCUE                                              ',
    'CCCCCCCCCCCCCCCCCC                                              ',
    'CCCCCCCCCCCCCCCCCC                                              ',
    'CCCCCCCCCCCCCCCCCC                                              ',
    'CCCCCCCCCCCCCCCCCC                                              ',
    'CCCCCCCCCCCCCCCCCC                                              ',
]

tileSize: int = 64
screenWidth: int = pygame.display.Info().current_w
screenHeight: int = len(map1) * tileSize
screenRealHeight: int = pygame.display.Info().current_h