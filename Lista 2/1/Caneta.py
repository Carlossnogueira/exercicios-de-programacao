"""
Caneta  que  deve  possuir  como  características  marca,  cor  e  tamanho.
"""

class Caneta:
    def __init__(self,marca,cor,tamanho):
        self._marca = marca
        self._cor = cor
        self._tamanho = tamanho
        
    def get_marca(self): 
        return self._marca
    
    def get_cor(self):
        return self._cor
    
    def get_tamanho(self):
        return self._tamanho 
    
    def set_marca(self,marca):
        self._marca = marca 
        
    def set_cor(self,cor):
        self._cor = cor 
        
    def set_tamanho(self,tamanho):
        self._tamanho = tamanho 
        
    def to_string(self):
        return f"Marca: {self._marca}, Cor: {self._cor}, Tamanho: {self._tamanho}"
    
    