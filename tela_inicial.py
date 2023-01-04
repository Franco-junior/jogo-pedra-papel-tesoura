import pygame
import time
from tela_palpite import *
from tela_jogo import *

pygame.init()

LARGURA = 600
ALTURA = 400
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('PEDRA, PAPEL E TESOURA')

state = 1

while state != 2:
    if state == 1:
        state = init_screen(janela)
    if state == 3:
        x = 0
    else:
        state = 2

pygame.quit()