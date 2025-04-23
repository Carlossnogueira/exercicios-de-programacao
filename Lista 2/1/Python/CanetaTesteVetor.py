from Caneta import Caneta

class CanetaTesteVetor:
    def __init__(self):
        self._canetas = []
        
    def cadastrar_caneta(self, caneta: Caneta):
        if len(self._canetas) < 50:
            self._canetas.append(caneta)
        else:
            print("Número maximo de canetas atingido!")
            
    def exibir_canetas(self):
        if not self._canetas:
            print("Nenhuma caneta cadastrada.")
        else:
            print("Canetas cadastradas:")
            # Forma de printar listas
            for i, caneta in enumerate(self._canetas, start=1):
                print(f"{i}. {caneta.to_string()}")

    def exibir_quantidade(self):
        if not self._canetas:
            print("0 canetas cadastradas no momento")
        else:
            print(f"{len(self._canetas)} caneta(s) cadastradas no total!")
            
    def exibir_por_cor(self,cor):
        if not self._canetas:
            print("Nenhuma caneta cadastrada para poder pesquisar!")
            return
        
        encontrou = False
        for caneta in self._canetas:
            if caneta.get_cor() == cor:  
                print(f"Caneta encontrada: {caneta.to_string()}")
                encontrou = True

        if not encontrou:
            print("Nenhuma caneta encontrada com essa cor.")
            