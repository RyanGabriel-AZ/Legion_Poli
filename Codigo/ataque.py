
import pygame


class Ataque(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, altura_tela,  velocidade):
        super().__init__()
        self.image = pygame.image.load('Imagens/ovo.jpeg').convert() # Carrega a imagem do ataque do personagem
        self.image.set_colorkey((0, 0, 0)) # Define a cor de fundo da imagem como transparente
        self.rect = self.image.get_rect(center = (pos_x, pos_y)) # Define a posição inicial do ataque do personagem
        self.velocidade = velocidade # Define a velocidade do ataque do personagem
        self.altura_tela = altura_tela
    
    def destruir(self):
        if self.rect.bottom < 0 or self.rect.top > self.altura_tela:
            self.kill()
        
    def update(self):
        self.rect.y -= self.velocidade
        self.destruir()