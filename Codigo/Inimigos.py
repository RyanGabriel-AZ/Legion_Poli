'''
Created on 5 de out. de 2025

@author: albuq
'''
import pygame

class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, limite_X , limite_Y):
        super().__init__()
        self.imagem = pygame.image.load('Imagens/Inimigo.png').convert_alpha() # Carrega a imagem do inimigo
        self.limite_X = limite_X # Define o limite X do inimigo
        self.limite_Y = limite_Y # Define o limite Y do inimigo
        self.velocidade = 4# Define a velocidade do inimigo
        self.rect = pygame.Rect(pos_x, pos_y, self.imagem.get_width(), self.imagem.get_height()) # Define a posição inicial do inimigo
    # o rect é um retângulo que envolve a imagem do inimigo e é usado para detectar colisões
        self.laser = True # Define se o inimigo pode atirar
    
    
    def atualizar(self):
        self.rect.y += self.velocidade