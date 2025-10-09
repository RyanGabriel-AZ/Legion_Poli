'''
Created on 5 de out. de 2025

@author: albuq
'''
import pygame

from Codigo.Laser import Laser


class Inimigo(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, limite_X , limite_Y):
        super().__init__()
        self.image = pygame.image.load('Imagens/nave.jpeg').convert() # Carrega a imagem do inimigo
        self.image.set_colorkey((0, 0, 0)) # Define a cor de fundo da imagem como transparente
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.limite_X = limite_X # Define o limite X do inimigo
        self.limite_Y = limite_Y # Define o limite Y do inimigo
        self.velocidade = 4# Define a velocidade do inimigo
        self.rect = self.image.get_rect(topleft = (pos_x,pos_y)) # Define a posição inicial do inimigo
    # o rect é um retângulo que envolve a imagem do inimigo e é usado para detectar colisões
        self.atirar = True # Define se o inimigo pode atirar
        self.tempo_ataque = 0 # Define o tempo de ataque do inimigo
        self.carregar_ataque = 5000 # Define o tempo de carregamento do ataque do inimigo
        self.largura = self.image.get_width()
        self.laser = pygame.sprite.Group() # Cria um grupo de lasers para o inimigo
        self.laser_som= pygame.mixer.Sound('Sons/laser.wav') # Carrega o som do laser
        self.laser_som.set_volume(0.1) # Define o volume do som do laser
        self.lasers = pygame.sprite.Group()

    def largura(self):
        return self.largura

    def recarga(self):
        if not self.atirar:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_ataque >= self.carregar_ataque:
                self.atirar = True

    def atirar_laser(self):
        if self.atirar:
            laser = Laser(self.rect.centerx, self.rect.top,7, self.limite_Y)
            self.lasers.add(laser)  # Adiciona um ataque ao grupo de ataques
            self.laser_som.play()
            self.pode_atirar = False
            self.tempo_ataque = pygame.time.get_ticks()
            # O ataque é criado na posição do personagem (self.rect.centerx, self.rect.top)
            # e se move para cima com velocidade 10

    def update(self):
        self.rect.y += self.velocidade
        self.atirar_laser()
        self.recarga()
        self.lasers.update()