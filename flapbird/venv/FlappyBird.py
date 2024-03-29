import pygame # biblioteca mais usada para criação de games
import os     # pra poder pegar percorrer os caminhos/pastas no sistema e pegar as imagens
import random # geração de números aleatórios (para posição dos canos)

SH = 500
SW = 800

IMG_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMG_BASE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMG_BKG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMGS_BRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
FONT_SCORE = pygame.font.SysFont('Arial', 50)