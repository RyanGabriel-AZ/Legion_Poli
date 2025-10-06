'''
Created on 5 de out. de 2025

@author: albuq
'''
import pygame
class AtaquePersonagem(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Imagens/AtaquePersonagem.png').convert_alpha() # Carrega a imagem do ataque do personagem
        self.rect = pygame.Rect(pos_x, pos_y, self.imagem.get_width(), self.imagem.get_height()) # Define a posição inicial do ataque do personagem
        self.velocidade = 9 # Define a velocidade do ataque do personagem
        
        
        
    def update(self):
        self.rect.y -= self.velocidade