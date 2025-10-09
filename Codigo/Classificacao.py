
import pygame
import heapq

from Estrutura_de_Dados import Fila


#nossos dados vao entrar na forma dado = (pontuacao, nome)
# "

#ranking.ordenar_elemento_decrescente((pontuacao, nome))

class classificacao():
    def __init__(self):


    def salvar_ranking_fila(fila, arquivo="ranking.ssv"):
        with open(arquivo, "w") as f:
            atual = fila.cabeca
            while atual:
                pontuacao, nome = atual.dado
                f.write(f"{nome};{pontuacao}\n")  # escreve no ssv
                atual = atual.proximo

    def carregar_ranking_fila(fila, arquivo="ranking.ssv"):
        try:  # vai tentar procurar a fila, caso não de certo, ele vai jogar uma excessão
            with open(arquivo, "r") as f:
                for linha in f:
                    nome, pontuacao = linha.strip().split(";")  # ele verifica as informações atraves da separação com ;
                    fila.ordenar_elemento_decrescente((int(pontuacao), nome))
        except FileNotFoundError:
            pass

    def mostrar_ranking_fila(screen, fila, font):
        screen.fill((0, 0, 0))  # tela preta
        y = 50  # altura
        atual = fila.cabeca
        pos = 1
        while atual:
            pontuacao, nome = atual.dado
            text = font.render(f"{pos}. {nome} - {pontuacao}", True,
                               (255, 255, 255))  # mostra o nome, posição e a pontuação em branco
            screen.blit(text, (100, y))  #
            y += 40  # vai descer a tela a cada while
            pos += 1  # ordem do lugar
            atual = atual.proximo
        pygame.display.flip()






