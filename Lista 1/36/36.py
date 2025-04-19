"""
Faça um programa que leia 10 valores inteiros e positivos e: 
- Encontre o maior valor 
- Encontre o menor valor 
- Calcule a média dos números lidos
"""

numero = []

for i in range(1,11):
    numero.append(int(input("Digite o número:"))) 
    
maior_numero = numero[0]
menor_numero = numero[0]
numeros = 0


for i in range(len(numero)):
  numeros += numero[i]

  if numero[i] > maior_numero:
    maior_numero = numero[i]
  if numero[i] < menor_numero:
    menor_numero = numero[i]
        
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
print(f"A média é de {numeros / len(numero)}")
        