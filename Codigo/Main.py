'''
Created on 5 de out. de 2025

@author: albuq
'''
import sys

import pygame

from Codigo.Inimigos import Inimigo
from Codigo.Jogador import Jogador
import random

if __name__ == '__main__':  # Inicia o jogo
    pygame.init()  # Inicializa o pygame
    tela_largura = 800
    tela_altura = 800
    tela = pygame.display.set_mode((tela_largura, tela_altura))  # Define o tamanho da tela
    fps = pygame.time.Clock()  # Controla os frames por segundo


class Game:
        def __init__(self):
            #habiitando jogador
            jogador_sprite = Jogador((tela_largura/2), tela_largura, tela_altura, tela_altura, 5)
            self.jogador = pygame.sprite.GroupSingle(jogador_sprite) #
            #vidas e pontuação implementar por final

            self.vidas = 1
            self.pontos = 0
            self.fonte =pygame.font.SysFont('arial', 20)

            #inimigos
            self.alien = pygame.sprite.Group()
            self.alien_lasers = pygame.sprite.Group()

            evento_alien= pygame.USEREVENT + 1
            pygame.time.set_timer(evento_alien, 1500)



            #extra




            #audio
            musica = pygame.mixer.Sound('musica.wav')
            musica.set_volume(0.2)
            musica.play(loops= -1) #fica tocando a musica em loop


        def colisoes(self):
            #jogador
            if self.jogador.sprite.ataque:
                for ataque in self.jogador.sprite.ataque:
                    alien_atingido = pygame.sprite.spritecollide(ataque, self.alien, True)
                    if alien_atingido:
                        for alien in alien_atingido:
                            self.pontos += 100
                        ataque.kill()
            #laser do alien
            if self.alien_lasers:
                for laser in self.alien_lasers:
                    if pygame.sprite.spritecollide(laser, self.jogador, False):
                        laser.kill()
                        pygame.quit()
                        #ranque()
                        sys.exit()
            #prorpio alien
            if self.alien:
                for alien in self.alien:
                    if    pygame.sprite.spritecollide(alien, self.jogador, False):
                            pygame.quit()
                            #ranque()
                            sys.exit()

        def po


class Main:

    
    
    
    
    









    if __name__ == '__main__': # Inicia o jogo
        pygame.init() # Inicializa o pygame
        tela_largura = 800
        tela_altura = 800
        tela = pygame.display.set_mode((tela_largura, tela_altura)) # Define o tamanho da tela
        fps = pygame.time.Clock() # Controla os frames por segundo
        