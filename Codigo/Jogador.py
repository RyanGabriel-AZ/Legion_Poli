'''
Created on 5 de out. de 2025

@author: albuq
'''
import pygame
class Jogador(pygame.sprite.Sprite):

    def __init__(self, posicao_x, controle_Max_x, velocidade):
        super().__init__()
        self.image = pygame.image.load('Imagens/Personagem.png').convert_alpha() # Carrega a imagem do personagem
        self.rect = self.image.get_rect(midbottom=(posicao_x, 600)) # Define a posição inicial do personagem
        self.controle_Max_x = controle_Max_x # Delimita a constante x maxima que o personagem pode ir
        self.velocidade = velocidade # Define a velocidade do personagem
        self.prontoAtaque = True
        self.prontoSpecial = True
        
        
        def entradas_jogador(self):
            keys = pygame.key.get_pressed() # Verifica as teclas pressionadas
            
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.velocidade # Move o personagem para a esquerda. o rect 
                #o rect é um retângulo que envolve a imagem do personagem e é usado para detectar colisões 
                # e movimentação.
            elif keys[pygame.K_RIGHT]:
                self.rect.x += self.velocidade
                