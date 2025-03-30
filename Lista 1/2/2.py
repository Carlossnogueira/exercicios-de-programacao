"""
Faça um programa que: 
- Leia a cotação do dólar 
- Leia um valor em dólares 
- Converta esse valor para Real 
- Mostre o resultado
"""

dolar = float(input("Digite a cotação do dolar"))
valorEmDolar = float(input("Digite o valor em dolar"))

convercao = dolar * valorEmDolar;

print(f"{valorEmDolar} USD em R$ fica: R$ ${round(convercao,2)}R$")
