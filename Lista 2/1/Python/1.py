"""
Implementar  uma  classe  Caneta  que  deve  possuir  como  características  marca,  cor  e  tamanho.  Nesta  classe 
devem ser implementados os  métodos construtores, getters, setters e toString. Em uma  outra classe 
chamada  CanetaTesteVetor  deverá  ser  criado  um  vetor  para  armazenar  no  máximo  50  objetos  do  tipo 
Caneta. O programa deverá exibir o seguinte menu para o usuário:  

1 – Cadastrar caneta 
2 – Exibir todas as canetas 
3 – Exibir quantidade de canetas cadastradas 
4 – Consultar quantidade de canetas de uma determinada cor (digitada pelo usuário) 
0 - Sair
"""

from CanetaTesteVetor import CanetaTesteVetor
from Caneta import Caneta

estoque_canetas = CanetaTesteVetor()

while True:
    
    print("---MENU DE OPÇÕES---")
    print("1 – Cadastrar caneta \n2 – Exibir todas as canetas\n3 – Exibir quantidade de canetas cadastradas\n4 – Consultar quantidade de canetas de uma determinada cor\n0 - Sair")
    
    try:
        entrada = int(input("Digite uma opção: \n"))
    except:
        print("entrada inválida!")
        continue
        
    match entrada:
        case 1:
            marca = input("Digite a marca:\n").lower()
            tamanho = input("Digite o tamanho:\n").lower()
            cor = input("Digite a cor:\n").lower()
            
            nova_caneta = Caneta(marca,cor,tamanho)
            estoque_canetas.cadastrar_caneta(nova_caneta)
        case 2:
            estoque_canetas.exibir_canetas()
        case 3:
            estoque_canetas.exibir_quantidade()
        case 4:
            cor = input("Digite a cor:\n").lower()
            estoque_canetas.exibir_por_cor(cor)
        case 0:
            print("Finalizando. . .")
            break
        case _:
            print("Algo deu errado!")