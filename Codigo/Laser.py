'''
Created on 5 de out. de 2025

@author: albuq
'''
import pygame
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Imagens/Laser.png').convert_alpha() # Carrega a imagem do laser
        self.rect = pygame.Rect(pos_x, pos_y, self.image.get_width(), self.image.get_height()) # Define a posição inicial do laser
        self.velocidade = 10 # Define a velocidade do laser
        
        
    def update(self):
        self.rect.y += self.velocidade