import pygame
import time
import random

LARGURA = 600
ALTURA = 400
FPS = 30
def game_screen(janela):
    clock = pygame.time.Clock()
    game = True

    pedra = pygame.image.load('Rock Pile.png').convert_alpha()
    pedra = pygame.transform.scale(pedra, (30,30))
    papel = pygame.image.load('scroll.png').convert_alpha()
    papel = pygame.transform.scale(papel, (30,30))
    tesoura = pygame.image.load('scissors_01.png').convert_alpha()
    tesoura = pygame.transform.scale(tesoura, (30,30))

    class Pedra(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = 200
            self.rect.y = 300
            #self.rect.x = random.randint(0, LARGURA-40)
            #self.rect.y = random.randint(0, ALTURA-40)
        
        def update(self) :
            hits = pygame.sprite.spritecollide(self, all_sprites, True, pygame.sprite.collide_rect_ratio(2.0))
            print(hits)
            if hits != []:
                self.rect.x = random.randint(0, LARGURA-40)
                self.rect.y = random.randint(0, ALTURA-40)
    
    class Papel(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = 200
            self.rect.y = 290
            #self.rect.x = random.randint(0, LARGURA-40)
            #self.rect.y = random.randint(0, ALTURA-40)

    class Tesoura(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, LARGURA-40)
            self.rect.y = random.randint(0, ALTURA-40)

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

    while game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                time.sleep(2)
        
        janela.fill((8, 91, 7))

        all_sprites.draw(janela)
        pygame.display.update()
    return 2