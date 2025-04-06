"""
Escreva um programa que exiba as seguintes opções e realize os que se pede em cada uma delas: 
1 – Adição 
2 – Subtração 
3 – Multiplicação 
4 – Divisão
"""

opcao = 0
numero1 = 0
numero2 = 0


try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o primeiro segundo: "))
except:
    print("Número inválido")
    exit()

    
while opcao <= 0:   
    print("---opções da calculadora---")
    print("1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão") 
    opcao = int(input("Digite a opção desejada:")) 

    if opcao == 1:
        print(f"{numero1} + {numero2} = {numero1+numero2}")
    elif opcao == 2:    
        print(f"{numero1} - {numero2} = {numero1-numero2}")
    elif opcao == 3:   
        print(f"{numero1} * {numero2} = {numero1*numero2}")
    elif opcao == 4:   
        print(f"{numero1} / {numero2} = {numero1/numero2}")
        
