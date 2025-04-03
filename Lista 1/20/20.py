"""
Escrever um programa declarando três variáveis do tipo inteiro (a, b e c). Ler um valor maior que zero para cada 
variável  (se  o  valor  digitado  não  é  válido,  mostrar  mensagem  e  ler  novamente).  Exibe  o  menor  valor  lido 
multiplicado pelo maior e o maior valor dividido pelo menor.
"""

def ler_valor(nome):
    while True:
        try:
            valor = int(input(f"Digite um valor inteiro positivo para {nome}: "))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser maior que zero.")
        except ValueError:
            print("Digite um número inteiro válido.")
            
def maior_valor(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return 0

def menor_valor(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
    else:
        return 0

a = ler_valor("A")
b = ler_valor("B")
c = ler_valor("C")

maior =  maior_valor(a,b,c) # ou max(a,b,c) - ai fica muito fácil
menor = menor_valor(a,b,c) # ou min(a,b,c)

multiplicacao = menor * maior
divisao = maior / menor

print(f"\nMenor valor ({menor}) multiplicado pelo maior ({maior}): {multiplicacao}")
print(f"Maior valor ({maior}) dividido pelo menor ({menor}): {divisao:.2f}")