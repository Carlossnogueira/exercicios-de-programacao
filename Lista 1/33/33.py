"""
Escreva um programa que calcule e exiba a média da nota dos alunos de uma turma em uma prova. O número de 
alunos é desconhecido. Os dados de um aluno são: número de matrícula e a sua nota na prova em questão.
"""

soma_notas = 0
media = 0
alunos_cadastrados = 0

while(True):
    try:
        print("--- Cadastro de Aluno: ---")
        entrada = int(input("1. Cadastrar novo\n2. Exibir média\n3. Sair."))
    except:
        print("Selecione uma opção válida!")
        continue
    
    match entrada:
        case 1:
            try:
                numero_matricula = int(input("Digite o número da matricula"))
                nota = int(input("Digite a nota do aluno"))
            except:
                print("Valor inválido informado!")
                continue
            soma_notas += nota
            alunos_cadastrados += 1
        case 2: 
            media = soma_notas / alunos_cadastrados
            print(f"A soma média dos alunos é de {media}, foram {alunos_cadastrados} aluno(s) cadastrados")
        case 3:
            exit()