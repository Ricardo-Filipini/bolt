import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Cores
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# Configurações do jogo
tamanho_bloco = 20
velocidade = 15

# Relógio do jogo
relogio = pygame.time.Clock()

# Fonte para pontuação
fonte = pygame.font.SysFont(None, 50)

def desenhar_cobra(tamanho_bloco, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura/6, altura/3])

def jogo_principal():
    game_over = False
    game_close = False

    # Posição inicial da cobra
    x = largura / 2
    y = altura / 2

    # Movimento inicial
    mudanca_x = 0
    mudanca_y = 0

    # Lista da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while not game_over:

        while game_close:
            tela.fill(preto)
            mensagem(f"Game Over! Pontuação: {comprimento_cobra - 1}. Pressione Q-Sair ou C-Jogar Novamente", vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo_principal()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    mudanca_x = -tamanho_bloco
                    mudanca_y = 0
                elif evento.key == pygame.K_RIGHT:
                    mudanca_x = tamanho_bloco
                    mudanca_y = 0
                elif evento.key == pygame.K_UP:
                    mudanca_y = -tamanho_bloco
                    mudanca_x = 0
                elif evento.key == pygame.K_DOWN:
                    mudanca_y = tamanho_bloco
                    mudanca_x = 0

        # Verificar colisão com bordas
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True

        x += mudanca_x
        y += mudanca_y
        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        
        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        lista_cobra.append(cabeca_cobra)
        
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verificar colisão própria
        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                game_close = True

        desenhar_cobra(tamanho_bloco, lista_cobra)
        
        pygame.display.update()

        # Verificar se comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

# Iniciar o jogo
jogo_principal()
