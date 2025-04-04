"""
Faça  um  programa  que  leia  um  número  inteiro  e  mostre  uma  mensagem  na  tela  indicando  se  este  número  é 
positivo ou negativo. Pare a execução do programa quando o usuário requisitar.
"""

def verificar_positivo_negativo(numero):
    if numero > 0:
        print("O número é positivo")
    else:
        print("O número é negativo")

numero = 0

while True:
    entrada = 0
    print("--Verificador de positivo ou negativo--")
    print("1. Começar\n2. Sair")
    try:
        entrada = int(input("Escolha uma opção:"))
        if entrada > 2:
            print("Nenhuma opção válida na entrada!")
    except:
        print("Nenhuma opção válida na entrada!")
    if entrada == 1:
         numero = int(input("Digite um número:"))
         verificar_positivo_negativo(numero)
    elif entrada == 2:
        print("Finalizando o sistema")
        exit()

   
    


