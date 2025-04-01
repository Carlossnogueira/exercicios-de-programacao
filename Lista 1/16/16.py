"""
Escreva um programa que leia dois números e exiba mensagem informando o valor do maior número e o valor do 
menor número. Se os dois números forem iguais, o programa deve exibir mensagem informando este fato.
"""

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    print("O primeiro número {} é maior que o segundo número {}" .format(primeiro_numero,segundo_numero))
elif primeiro_numero < segundo_numero:
    print("O primeiro número {} é menor que o segundo número {}" .format(primeiro_numero,segundo_numero))
elif primeiro_numero == segundo_numero:
    print("Os dois números são iguais!")
else:
    print("Números inválidos")