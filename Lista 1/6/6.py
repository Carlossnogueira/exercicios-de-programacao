"""
Ler uma temperatura em graus Celsius e apresentá-Ia convertida em graus Fahrenheit. A fórmula de conversão de 
temperatura  a  ser  utilizada  é  F  =  (9  *  C  +  160)  /  5,  em  que  a  variável  F  representa  é  a  temperatura  em  graus 
Fahrenheit e a variável C representa é a temperatura em graus Celsius. 
"""

C = int(input("Digite a temperadura em Graus Celcius: "))
F = (9 * C + 160 ) / 5;

print(f"A converção de {C}° em Fahrenheit é de {F}")