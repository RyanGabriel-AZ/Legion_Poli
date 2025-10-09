'''
Created on 5 de out. de 2025

@author: albuq
'''

import sys
import pygame
import random

import self

from Codigo.Estrutura_de_Dados import Fila
from Codigo.Jogador import Jogador
from Codigo.Inimigos import Inimigo


# Configurações da tela
Largura_tela = 800
Altura_tela = 800
FPS = 60 # o FPS está atrelado ao clock

#Configurações do ranking
ranking_maximo = 10
ranking = Fila(ranking_maximo) # Aqui criamos a fila, que ira armazenar nosso rank

#vamos criar as funcionalidades do hanking e implemntar as filas com ssv e o pygame
def carregar_ranking_fila(fila, arquivo="Ranking/ranking.ssv"):
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                nome, pontuacao = linha.strip().split(";")
                fila.ordenar_elemento_decrescente((int(pontuacao), nome))
    except FileNotFoundError:
        pass

def salvar_ranking_fila(fila, arquivo="Ranking/ranking.ssv"):
    with open(arquivo, "w") as f:
        atual = fila.cabeca
        while atual:
            pontuacao, nome = atual.dado
            f.write(f"{nome};{pontuacao}\n")
            atual = atual.proximo


class Game:
    def __init__(self, tela):
        self.tela = tela
        self.clock = pygame.time.Clock()
        parametro = Inimigo(0,0,0,0)
        self.fundo = pygame.image.load("Imagens/ceu.jpeg").convert()
        self.fundo = pygame.transform.scale(self.fundo, (self.tela.get_width(), self.tela.get_height()))
        # Definindo o Jogador
        jogador_sprite = Jogador((Largura_tela/2),Largura_tela, Altura_tela, Altura_tela, 4)
        self.jogador = pygame.sprite.GroupSingle(jogador_sprite)

        # Inimigos
        self.alien = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()

        # Pontuação
        self.pontos = 0
        self.fonte = pygame.font.SysFont('arial', 30)

        # Evento de spawn de aliens
        self.EVENTO_ALIEN = pygame.USEREVENT + 1
        pygame.time.set_timer(self.EVENTO_ALIEN, 1500) #Aqui manipulamos de quanto em quanto tempo o alien nasce

        # Carregar ranking
        carregar_ranking_fila(ranking)

    # --- Spawn de alien aleatório ---
    def spawn_alien(self): #Aqui faremos um spawn aleatorio de alien, na posicao x, y=0
        x_pos = random.randint(0, (Largura_tela-Inimigo(0,0,0,0).largura))
        novo_alien = Inimigo(x_pos, 0, Largura_tela, Altura_tela)  # velocidade 3
        self.alien.add(novo_alien)

    # --- Colisões ---
    def colisoes(self):
        # Laser do jogador acerta alien
        if self.jogador.sprite.ataque:
            for ataque in self.jogador.sprite.ataque:
                aliens_atingidos = pygame.sprite.spritecollide(ataque, self.alien, True) #a funcção verifica colisoes
                if aliens_atingidos:
                    self.pontos += 100 * len(aliens_atingidos) #Quanto mais aliens mais pontos
                    ataque.kill()

        # Alien atinge jogador
        for laser in self.alien_lasers: #laser do alien atinge jogador
            if pygame.sprite.spritecollide(laser, self.jogador, False):
                laser.kill()
                self.fim_jogo()
        for alien in self.alien: #alien atinge jogador
            if pygame.sprite.spritecollide(alien, self.jogador, False):
                self.fim_jogo()

    #Aqui pedimos o nome do usuario, para completar o ranking
    def pedir_nome(self):
        nome = ""
        input_box = pygame.Rect(200, 350, 400, 50) # fez um quadrado com colisoes
        active = True
        font = pygame.font.SysFont(None, 40)

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #jogador fechou a janela
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: #aperta o enter, envia o que foi digitado
                    if event.key == pygame.K_RETURN and nome.strip() != "":
                        active = False
                    elif event.key == pygame.K_BACKSPACE: #aperta o back, e apaga o ultimo caracttere
                        nome = nome[:-1]
                    else:
                        nome += event.unicode #unicode guarda letras pressionadas, vai adicionando a o nome

            self.tela.fill((0,0,0)) #tela preta
            txt_surface = font.render(nome, True, (255,255,255))# textoo branco
            self.tela.blit(txt_surface, (input_box.x+5, input_box.y+5)) # blit serve para desenhar o texto
            pygame.draw.rect(self.tela, (255,255,255), input_box, 2) # desenha a borda da caixa
            pygame.display.flip() #atualiza a tela a cada frame
            self.clock.tick(30) #contador de fps

        return nome

    #Fim do jogo
    def fim_jogo(self):
        nome = self.pedir_nome()
        ranking.ordenar_elemento_decrescente((self.pontos, nome))
        salvar_ranking_fila(ranking)
        self.mostrar_ranking()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

    # Mostrar ranking
    def mostrar_ranking(self):
        self.tela.fill((0,0,0))
        y = 50
        atual = ranking.cabeca
        pos = 1
        while atual:
            pontuacao, nome = atual.dado
            text = self.fonte.render(f"{pos}. {nome} - {pontuacao}", True, (255,255,255))
            self.tela.blit(text, (200, y))
            y += 40
            pos += 1
            atual = atual.proximo
        pygame.display.flip()

    def atualizar_pontos(self):
        tempo_passado = (pygame.time.get_ticks() - self.tempo_inicial)//1000
        self.pontos += tempo_passado*10

    #  Loop principal ---
    def run(self):
        self.tempo_inicial = pygame.time.get_ticks()
        while True:
            self.tela.blit(self.fundo, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  #verifica saida do jogo
                    pygame.quit()
                    sys.exit()
                if event.type == self.EVENTO_ALIEN: #lanca alien
                    self.spawn_alien()

            self.jogador.update()
            self.alien.update()
            self.alien_lasers.update()
            self.colisoes()
            self.atualizar_pontos()

            # Desenhar

            self.jogador.draw(self.tela) #desenha o jogador
            self.alien.draw(self.tela) #desenha oo alien
            self.alien_lasers.draw(self.tela) #o ataque
            pontos_text = self.fonte.render(f"Pontos: {self.pontos}", True, (255,255,0))
            self.tela.blit(pontos_text, (10,10))

            pygame.display.flip()
            self.clock.tick(FPS)

#Main
if __name__ == '__main__':
    pygame.init()
    tela = pygame.display.set_mode((Largura_tela, Altura_tela))
    game = Game(tela)
    game.run()


