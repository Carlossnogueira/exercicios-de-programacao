"""
Escreva um programa que leia quatro notas escolares de um aluno e apresentar uma mensagem que o aluno foi 
aprovado se o valor da média escolar for maior ou igual a 7. Se o valor da média for menor que 7, solicitar a nota 
do  recuperação,  somar  com  o  valor  da  média  e  obter  a  nova  média.  Se  a  nova  média  for  maior  ou  igual  a  7, 
apresentar  uma  mensagem  informando  que  o  aluno  foi  aprovado  na  recuperação.  Se  o  aluno  não  foi  aprovado, 
apresentar  uma mensagem  informando  esta  condição.  Apresentar  junto  com  as mensagens  o  valor  da  média  do 
aluno.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Dite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("O aluno foi aprovado!")
else:
    nota_recuperacao = float(input("Aluno reprovado! Digite a nota de recuperação para a nova média: "))
    nova_media = (media + nota_recuperacao) / 2
    if nova_media >= 7:
        print("Usuario aprovado na recuperação!")
    else:
        print(f"Aluno não aprovado! a média é menor do que o nescessário. Média do aluno {media} de 7")
    