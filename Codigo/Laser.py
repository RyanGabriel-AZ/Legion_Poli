'''
Created on 5 de out. de 2025

@author: albuq
'''
import pygame


class Laser(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, velocidade, altura_tela):
        super().__init__()
        self.image = pygame.Surface((5, 10)) # Tamanho do laser
        self.image.fill((255, 0, 0))  # Cor vermelha para o laser
        self.rect = self.image.get_rect(center=(pos_x,pos_y)) # Posição inicial do laser
        self.velocidade = velocidade  # Velocidade do laser (negativa para cima, positiva para baixo)
        
        self.altura_tela = altura_tela  # Altura da tela para remover o laser quando sair da tela
    
    
    def destruir(self):
        if self.rect.bottom < 0 or self.rect.top > self.altura_tela: # Verifica se o laser saiu da tela
            self.kill() # Remove o laser do grupo de sprites
            
    def update(self):
        self.rect.y += self.velocidade
        self.destruir()