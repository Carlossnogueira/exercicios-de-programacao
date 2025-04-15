"""
Escreva  um  programa  que  calcule  e  exiba  a  soma  dos  quadrados  dos  20  primeiros  números  inteiros  positivos 
ímpares a partir do número informado pelo usuário menor que 10 e maior que zero.
"""


numero = int(input("Digite um número inteiro entre 1 e 9: "))


if numero <= 0 or numero >= 10:
    print("Número inválido! Deve ser maior que 0 e menor que 10.")
else:
    contador = 0
    soma_quadrados = 0
    atual = numero

    while contador < 20:
        if atual % 2 != 0:  # Se for ímpar
            soma_quadrados += atual ** 2
            contador += 1
        atual += 1  # Próximo número

    print(f"A soma dos quadrados dos 20 primeiros números ímpares a partir de {numero} é: {soma_quadrados}")
