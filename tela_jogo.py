import pygame
import time
from random import *

LARGURA = 600
ALTURA = 400
FPS = 30
def game_screen(janela):
    clock = pygame.time.Clock()
    game = True

    pedra = pygame.image.load('rock_round.png').convert_alpha()
    pedra = pygame.transform.scale(pedra, (30,15))
    papel = pygame.image.load('rock_round.png').convert_alpha()
    papel = pygame.transform.scale(papel, (30,15))
    tesoura = pygame.image.load('rock_round.png').convert_alpha()
    tesoura = pygame.transform.scale(tesoura, (30,15))

    class Pedra(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, LARGURA-30)
            self.rect.y = random.randint(0, ALTURA-30)
    
    class Papel(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, LARGURA-30)
            self.rect.y = random.randint(0, ALTURA-30)

    class Tesoura(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, LARGURA-30)
            self.rect.y = random.randint(0, ALTURA-30)

    all_sprites = pygame.sprite.Group()
    all_pedra = pygame.sprite.Group()
    all_papel = pygame.sprite.Group()
    all_tesoura = pygame.sprite.Group()

    pedraa = Pedra(pedra)
    papell = Papel(papel)
    tesouraa = Tesoura(tesoura)

    all_sprites.add(pedraa)
    all_sprites.add(papell)
    all_sprites.add(tesouraa)
    all_pedra.add(pedraa)
    all_papel.add(papell)
    all_tesoura.add(tesouraa)