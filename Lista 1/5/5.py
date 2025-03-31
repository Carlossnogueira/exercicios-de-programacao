"""
Efetuar o cálculo da quantidade  de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 
12  Km  por  litro.  Para  obter  o  cálculo,  o  usuário  deve  fornecer  o  tempo  gasto  na  viagem  e  a  velocidade  média. 
Desta  forma,  será  possível  obter  a  distância  percorrida  com  a  fórmula  DISTANCIA  =  TEMPO  *  VELOCIDADE. 
Tendo  o  valor  da  distância,  basta  calcular  a  quantidade  de  litros  de  combustível  utilizada  na  viagem  com  a 
fórmula:  LITROS_USADOS  =  DISTANCIA  /  12.  O  programa  deve  apresentar  os  valores  da  velocidade  média, 
tempo gasto, a distância percorrida e a quantidade de litros utilizada na viagem. Dica: trabalhe com valores reais.
"""

autonomia = 12

tempo_gasto = int(input("Digite o tempo da viagem em horas: "))
velocidade_media = int(input("Digite a velocidade média da viagem: "))

distancia = velocidade_media * tempo_gasto
litros_usados = distancia / autonomia

print(f"Velocidade média {velocidade_media} Km/h")
print(f"Tempo gasto {tempo_gasto} horas")
print(f"Distância percorrida: {distancia} Km")
print(f"Litros usados: {litros_usados} litros")