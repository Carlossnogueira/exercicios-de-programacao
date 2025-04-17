"""
Escreva  um  programa  que  leia  um  conjunto  de  números  positivos  e  exiba  o  menor  e  o  maior.  Suporemos  que  o 
número de elementos deste conjunto  não é conhecido, e que um número negativo será  utilizado para sinalizar  o 
fim dos dados. 
"""

numeros = []

while True:
    try:
        entrada = int(input("Digite um número (negativo para sair): "))
    except:
        print("Entrada inválida. Digite apenas números inteiros.")
        continue

    if entrada < 0:
        break
    else:
        numeros.append(entrada)

if numeros:
    maior_numero = numeros[0]
    menor_numero = numeros[0]

    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero

    print("Maior número:", maior_numero)
    print("Menor número:", menor_numero)
else:
    print("Nenhum número positivo foi digitado.")

