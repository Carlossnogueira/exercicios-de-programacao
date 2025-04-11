"""
Escrever um programa que leia um conjunto de números positivos, e exiba se o número lido é par ou ímpar. Exiba 
ao final a soma total dos números pares lidos e também a soma dos números ímpares lidos. Suporemos que o 
número de elementos deste conjunto não é conhecido, e que um número negativo será utilizado para sinalizar o 
fim dos dados. 
"""

numeros_positivos = []
numeros_impares = []
numeros_pares = []

soma_pares = 0
soma_impares = 0

while True:
    entrada = int(input("Digite um número positivo (ou um número negativo para encerrar): "))
    
    if entrada < 0:
        break

    numeros_positivos.append(entrada)

    if entrada % 2 != 0:
        print(f"Número {entrada} é ímpar")
        numeros_impares.append(entrada)
        soma_impares += entrada
    else:
        print(f"Número {entrada} é par")
        numeros_pares.append(entrada)
        soma_pares += entrada

print(f"A soma dos pares é {soma_pares} e dos ímpares é: {soma_impares}")
