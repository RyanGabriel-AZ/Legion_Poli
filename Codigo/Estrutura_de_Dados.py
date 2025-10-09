class No():
   
 


    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaEncandeada():
       
    
    def __init__(self, limite):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        self.limite = limite
        
    def  limite_lista(self, limite):
        self.limite = limite
    
    
    
    def cauda_lista(self):
        return self.cauda.dado
    
    def cabeca_lista(self):
        return self.cabeca.dado
    
    def vazio(self):
        if self.tamanho == 0:
            return True   
    
    def inserir_final(self, dado):
        # adiciona no final da lista
        elemento = No(dado)
        if self.cabeca is None:
            self.cabeca = self.cauda = elemento 
           
            
            self.cabeca.anterior = None
            self.cauda.proximo = None
            
            self.tamanho += 1
        else:
            self.cauda.proximo = elemento
            elemento.anterior = self.cauda
            self.cauda= elemento
            self.cauda.proximo = None
            
            self.tamanho += 1
        return 
    
    def inserir_inicio(self, dado):
        # adiciona no inicio da lista
        elemento = No(dado)
        if self.cabeca is None:
            self.cabeca = self.cauda = elemento 
           
            
            self.cabeca.anterior = None
            self.cauda.proximo = None
            
            self.tamanho += 1
        else:
            elemento.proximo = self.cabeca
            self.cabeca.anterior = elemento
            self.cabeca= elemento
            self.cabeca.anterior = None
            
            self.tamanho += 1
        return
    
    def remover(self, dado):
        
        if  not self.vazio():
            if self.cabeca.dado == dado and self.tamanho == 1:
                self.cabeca = self.cauda =  None
                
                
                self.tamanho -= 1
            elif self.cabeca.dado == dado:
                self.cabeca = self.cabeca.proximo
                self.cabeca.anterior = None
             
                self.tamanho -= 1
            else:
              
                atual = self.cabeca
                anterior = self.cauda.anterior
                while atual.proximo is not None:
                    if atual.dado == dado:
                        anterior.proximo = atual.proximo
                        atual.proximo.anterior = anterior
                        self.tamanho -= 1
                        break
                    else:
                        anterior = atual
                        atual = atual.proximo

                    break
            
    def remover_inicio(self):
        
        if  not self.vazio():
            if  self.tamanho == 1:
                self.cabeca = self.cauda =  None
                
            else: 
                self.cabeca = self.cabeca.proximo 
                self.cabeca.anterior = None        

                self.tamanho -= 1
            return
    def remover_final(self):
        if  not self.vazio():
            if  self.tamanho == 1:
                self.cabeca = self.cauda =  None
            else:
                self.cauda= self.cauda.anterior
                self.cauda.proximo = None
                
                self.tamanho -= 1
                

class Deque(ListaEncandeada):
    def __init__(self):
        super().__init__()
        
    def inserir_inicio(self, dado):
        super().inserir_inicio(dado)
        
    def inserir_final(self, dado):
        super().inserir_final(dado)
        
    def remover_inicio(self):
        super().remover_inicio()
        
    def remover_final(self):
        super().remover_final()
        
        
class Fila(ListaEncandeada):
    def __init__(self, limite):
        super().__init__(limite)
        self.limite = limite
        
        
        
    def tamanho_max_fila(self, limite):
        super().limite_lista(limite)
    
    def inserir(self, dado):
        return self.inserir_final(dado)
    def remover(self):
        return self.remover_inicio()   
    def remover_duplicatas(self):
        lista = ListaEncandeada()
        atual = self.cabeca

        while atual:
            dado = atual.dado

        # Verificar se o dado já está em lista
            ja_existe = False
            verificador = lista.cabeca
            while verificador:
                if verificador.dado == dado:
                    ja_existe = True
                    break
                verificador = verificador.proximo

        # Se não existe, adiciona à nova lista
            if not ja_existe:
                lista.inserir_final(dado)

                atual = atual.proximo

        return lista
    
    
    def limite__fila(self, ):
        if self.tamanho > self.limite:
            while self.tamanho > self.limite:
                self.remover_final()
        return
    
    def ordenar_elemento_decrescente(self, dado):
        if self.vazio():
            self.inserir_inicio(dado)
            return
        else:
            if dado >= self.cabeca.dado:
                self.inserir_inicio(dado)
                self.limite__fila()
                return
            elif dado <= self.cauda.dado and self.tamanho == self.limite:
                return
            elif dado <= self.cauda.dado: # Gabiarra estilo Deque
                super().inserir_final(dado)

            else:
                no = No(dado)
                atual = self.cabeca
                while atual.proximo is not None:
                    if dado >= atual.proximo.dado:
                        atual.proximo.anterior= no
                        atual.proximo= no
                        no.anterior = atual
                        no.proximo = atual.proximo.proximo
                        self.tamanho += 1
                        self.limite__fila()
                        break
                    atual = atual.proximo   
                return
        