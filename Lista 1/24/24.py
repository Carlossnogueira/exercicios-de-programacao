"""
Escreva  um  programa  que  leia  dois  números  inteiros  e  apresente  as  opções  para  usuário  escolher  o  que  deseja 
realizar: 
1 – Verificar se um dos números lidos é ou não múltiplo do outro 
2 – Verificar se os dois números lidos são pares 
3 – Verificar se a média dos dois números é maior ou igual a 7. 
4 – Sair
"""

opcao = 0
numero1 = 0
numero2 = 0
loop = True

while loop:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o primeiro segundo: "))
        loop = False
    except:
        print("Número inválido")
        
    
while opcao <= 0:   
    print("---opções da calculadora---")
    print("1. Verificar se são multiplos\n2. Verificar pares e impares\n3. Verificar se média é maior que 7\n4. Sair") 
    opcao = int(input("Digite a opção desejada:")) 

    match opcao:
        case 1:
            if numero1 % numero2 == 0 or numero2 % numero1 == 0:
                print(f"Os números {numero1} e {numero2} são multiplos")
            else:
                print(f"Os números {numero1} e {numero2} não são multiplos")
        case 2:
            if numero1 % 2 == 0 and numero2 % 2 == 0:
                print(f"número {numero1} e número {numero2} são pares")
            elif numero1 % 2 > 0 and numero2 % 2 > 0:
                print(f"número {numero1} e número {numero2} são impares")
            elif numero1 % 2 > 0 and numero2 % 2 == 0:
                print(f"número {numero1} é impar e número {numero2} é par")
            elif numero1 % 2 == 0 and numero2 % 2 > 0:
                print(f"número {numero1} é par e número {numero2} é impar")
            else:
                print("Erro")
        case 3:
            
            if (numero1 + numero2) / 2 > 7:
                print(f"A média é maior que 7,media = {(numero1 + numero2) / 2}")
            else:
                print(f"A média não é maior que 7,media = {(numero1 + numero2) / 2}")
        case 4:
            exit()
        case _:
            print("Nenhuma opção válida")