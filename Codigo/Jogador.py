
import pygame
from ataquePersonagem import AtaquePersonagem


class Jogador(pygame.sprite.Sprite):

        def __init__(self, posicao_x, controle_Max_x,posicao_y, controle_Max_y,  velocidade):
            super().__init__()
            self.image = pygame.image.load('Imagens/galinha.jpeg').convert() # Carrega a imagem do personagem
            self.image.set_colorkey((0, 0, 0)) # Define a cor de fundo da imagem como transparente
            self.image = pygame.transform.scale(self.image, (50,50))
            self.rect = self.image.get_rect(midbottom=(posicao_x, posicao_y)) # Define a posição inicial do personagem
            self.controle_Max_x = controle_Max_x # Delimita a constante x maxima que o personagem pode ir
            self.velocidade = velocidade # Define a velocidade do personagem
            self.controle_Max_y = controle_Max_y # Delimita a constante y maxima que o personagem pode ir
            self.prontoAtaque = True
            self.prontoSpecial = True
            self.tempo_ataque = 0 # Define o tempo de ataque do personagem
            self.carregar_ataque = 200 # Define o tempo de carregamento do ataque do personagem
        
            self.ataque = pygame.sprite.Group() # Cria um grupo de ataques para o personagem
        
            self.ataque_som= pygame.mixer.Sound('Sons/ovo.wav') # Carrega o som do ataque
            self.ataque_som.set_volume(0.5) # Define o volume do som do ataque
        
        
        def limites_tela(self):
            if self.rect.x < 0: # Impede que o personagem saia da tela
                self.rect.x = 0
            elif self.rect.x > self.controle_Max_x - self.rect.width: # - self.rect.width para considerar a largura do personagem
                self.rect.x = self.controle_Max_x - self.rect.width
            elif self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.y > self.controle_Max_y - self.rect.height:
                self.rect.y = self.controle_Max_y - self.rect.height
            else: 
                return
        
        def entradas_jogador(self):
            keys = pygame.key.get_pressed() # Verifica as teclas pressionadas
            
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.velocidade # Move o personagem para a esquerda. o rect 
                self.limites_tela()
                #o rect é um retângulo que envolve a imagem do personagem e é usado para detectar colisões 
                # e movimentação.
            elif keys[pygame.K_RIGHT]:
                self.rect.x += self.velocidade
                self.limites_tela()
                
            elif keys[pygame.K_UP]:
                self.rect.y -= self.velocidade
                self.limites_tela()
                
            elif keys[pygame.K_DOWN]:
                self.rect.y += self.velocidade
                self.limites_tela()
                
            elif keys[pygame.K_z] and self.prontoAtaque:
                self.atacar()
                self.prontoAtaque = False
                self.tempo_ataque = pygame.time.get_ticks() # Reinicia o tempo de ataque
                self.ataque_som.play()
        def recarga(self):
            if not self.prontoAtaque:
                tempo_atual = pygame.time.get_ticks()    
                if tempo_atual - self.tempo_ataque >= self.carregar_ataque: 
                    self.prontoAtaque = True    
                    
                    
        def atacar(self):
            if self.prontoAtaque:
                Ataque = AtaquePersonagem(self.rect.centerx, self.rect.top, self.controle_Max_y, 3)
                self.ataque.add(Ataque) # Adiciona um ataque ao grupo de ataques
                # O ataque é criado na posição do personagem (self.rect.centerx, self.rect.top)
                # e se move para cima com velocidade 10
                
        def update(self):
            self.entradas_jogador()
            self.limites_tela()
            self.recarga()
            
            