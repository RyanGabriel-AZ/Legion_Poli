
import pygame
import heapq

from Estrutura_de_Dados import Fila







def salvar_ranking_fila(fila, arquivo="ranking.ssv"):
    with open(arquivo, "w") as f:
        atual = fila.cabeca
        while atual:
            pontuacao, nome = atual.dado
            f.write(f"{nome};{pontuacao}\n")
            atual = atual.proximo

def carregar_ranking_fila(fila, arquivo="ranking.ssv"):
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                nome, pontuacao = linha.strip().split(";")
                fila.ordenar_elemento_decrescente((int(pontuacao), nome))
    except FileNotFoundError:
        pass


def mostrar_ranking_fila(screen, fila, font):
    screen.fill((0,0,0))
    y = 50
    atual = fila.cabeca
    pos = 1
    while atual:
        pontuacao, nome = atual.dado
        text = font.render(f"{pos}. {nome} - {pontuacao}", True, (255,255,255))
        screen.blit(text, (100, y))
        y += 40
        pos += 1
        atual = atual.proximo
    pygame.display.flip()




