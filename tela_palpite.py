import pygame
import time
FPS = 60
palpite = ''

def init_screen (janela):
    font = pygame.font.SysFont('Comics', 35)
    text1 = font.render('Pedra', True, (0, 0, 255))
    text2 = font.render('Papel', True, (0, 0, 255))
    text3 = font.render('Tesoura', True, (0, 0, 255))
    mode = font.render('Faça seu palpite de quem irá ganhar!!!', True, (0, 0, 0))
    clock = pygame.time.Clock()
    game = True
    
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if botao1.collidepoint((x,y)):
                    state = 3
                    game = False
                elif botao2.collidepoint((x,y)):
                    state = 3
                    game = False
                elif botao3.collidepoint((x,y)):
                    state = 3
                    game = False
            if event.type == pygame.QUIT:
                game = False
                state = 2
                time.sleep(2)
            
            janela.fill((8, 91, 7))
            cor = (255, 255, 0)
            
            #criando os botões
            vertices1 = [(75, 300), (175, 300), (175, 350), (75, 350)]
            vertices2 = [(250, 300), (350, 300), (350, 350), (250, 350)]
            vertices3 = [(425, 300), (525, 300), (525, 350), (425, 350)]
            botao1 = pygame.draw.polygon(janela, cor, vertices1)
            botao2 = pygame.draw.polygon(janela, cor, vertices2)
            botao3 = pygame.draw.polygon(janela, cor, vertices3)
        
            #alterando posição dos textos
            #janela.blit(background, (190, 60))
            janela.blit(mode, (80, 150))
            janela.blit(text1, (92, 313))
            janela.blit(text2, (268, 314))
            janela.blit(text3, (430, 315))
            #background = pygame.transform.scale(background, (200, 160))
            pygame.display.flip()
    
    return state