'''
Created on 5 de out. de 2025

@author: albuq
'''
import pygame

class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, limite_X , limite_Y):
        super().__init__()
        self.imagem = pygame.image.load('Imagens/nave.jpeg').convert_alpha() # Carrega a imagem do inimigo
        self.image.set_colorkey((0, 0, 0)) # Define a cor de fundo da imagem como transparente
        self.limite_X = limite_X # Define o limite X do inimigo
        self.limite_Y = limite_Y # Define o limite Y do inimigo
        self.velocidade = 4# Define a velocidade do inimigo
        self.rect = self.image.get_rect(topleft = (pos_x,pos_y)) # Define a posição inicial do inimigo
    # o rect é um retângulo que envolve a imagem do inimigo e é usado para detectar colisões
        self.atirar = True # Define se o inimigo pode atirar
        self.tempo_ataque = 0 # Define o tempo de ataque do inimigo
        self.carregar_ataque = 500 # Define o tempo de carregamento do ataque do inimigo
        
        self.laser = pygame.sprite.Group() # Cria um grupo de lasers para o inimigo
        self.laser_som= pygame.mixer.Sound('Sons/laser_som.wav') # Carrega o som do laser
        self.laser_som.set_volume(0.2) # Define o volume do som do laser
    
    def update(self):
        self.rect.y += self.velocidade