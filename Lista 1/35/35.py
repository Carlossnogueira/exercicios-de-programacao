"""
Faça um programa que conte de 1 até 100 e a cada múltiplo de 10 exiba uma mensagem: "Múltiplo de 10".
"""

for i in range(1,101):
    if i% 10 >= 0.1 :
        print(i)
    if i % 10 == 0:
        print(f"Multiplo de 10: {i}")