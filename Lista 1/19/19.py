"""
Escreva  um  programa  que  leia  três  valores  para  os  lados  de  um  triângulo  (variáveis  A,  B  e  C).  Verificar  se  cada 
lado é menor que a soma dos outros dois lados. Se sim, saber de A==B e se B==C, sendo verdade o triângulo é 
eqüilátero;  Se  não,  verificar  de  A==B  ou  se  A==C  ou  se  B==C,  sendo  verdade  o  triângulo  é  isósceles;  e  caso 
contrário,  o  triângulo  será  escaleno.  Caso  os  lados  fornecidos  não  caracterizarem  um  triângulo,  avisar  a 
ocorrência.
"""

A = float(input("Digite o lado A: "))
B = float(input("Digite o lado B: "))
C = float(input("Digite o lado C: "))

if A < B + C and B < A + C and C < A + B:
    if A == B and B == C:
         print("Triângulo Equilátero")
    elif A == B or A == C or B == C:
         print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores fornecidos não formam um triângulo.")