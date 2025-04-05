"""
Faça um programa que leia um número. Se positivo  armazene-o em A, se for negativo, em B. No final mostrar o 
resultado.
"""
a = 0
b = 0

try:
    numero = int(input("Digite um número: "))
except:
    print("Número inválido!")

if numero > 0:
    a = numero
else:
    b = numero

print(f"A = {a} e B = {b}")