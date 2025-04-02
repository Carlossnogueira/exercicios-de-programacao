"""
Escreva um programa que leia um número inteiro. Verificar por meio de condição se o valor fornecido está na faixa 
entre  0  (zero)  e  9  (nove).  Caso  o  valor  fornecido  esteja  dentro  da  faixa,  apresentar  a  mensagem  “valor  válido”. 
Caso contrário, apresentar a mensagem “valor inválido”. 
"""

numero = int(input("Digite o número: "))

if numero <= 9 and numero >= 0:
    print("valor  válido")
else:
    print("valor inválido")