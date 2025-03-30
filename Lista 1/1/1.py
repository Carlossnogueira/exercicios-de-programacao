"""
Faça um programa para calcular o estoque médio de uma peça, sendo que: 
ESTOQUE MÉDIO = (QUANTIDADE_MÍNIMA + QUANTIDADE_MÁXIMA) / 2. 
"""

quantMinima = float(input("Digite a quantidade minima"))
quantMaxima = float(input("Digite a quantidade  máxima"))
estoqueMedio = (quantMinima + quantMaxima) / 2
print("O estoque mínimo é de: " + str(estoqueMedio))