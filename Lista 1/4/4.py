"""
Ler  quatro  valores  numéricos  inteiros  e  apresentar  o  resultado  dois  a  dois  da  adição  e  multiplicação  entre  os 
valores lidos, baseando-se na utilização do conceito de propriedade distributiva. Dica: se forem lidas as variáveis 
A, B, C e D, devem ser somados e multiplicados os valores de A com B, A com C e A com D; depois B com C, B 
com  D  e  por  último  C  com  D.  Note  que  para  cada  operação  serão  utilizadas  seis  combinações.  Assim  sendo, 
devem ser realizadas doze operações de processamento, sendo seis para as adições e seis para as 
multiplicações.
"""

def calcular_operacoes(valores: list[int]):
    for i in range(len(valores) - 1):
        for j in range(i + 1, len(valores)):
            print(f"Valor {i + 1} e Valor {j + 1}:")
            print(f"\t{valores[i]} + {valores[j]} = {valores[i] + valores[j]}")
            print(f"\t{valores[i]} * {valores[j]} = {valores[i] * valores[j]}\n")

valores = []
valor1 = int(input("Digite o primeiro valor:"))
valores.append(valor1)
valor2 = int(input("Digite o segundo valor:"))
valores.append(valor2)
valor3 = int(input("Digite o terceiro valor:"))
valores.append(valor3)
valor4 = int(input("Digite o quarto valor:"))
valores.append(valor4)

calcular_operacoes(valores)
    
 





    