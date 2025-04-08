"""
Tendo  como  dados  de  entrada  a  altura  e  o  sexo  de  uma  pessoa,  faça  um  programa  que  calcule  seu  peso  ideal, 
utilizando as seguintes fórmulas: (h = altura) 
- Para homens: (72.7*h) - 58 
- Para mulheres: (62.1 *h) - 44.7
"""

opcao = False

while True:
    genero = input("Digite seu gênero (M/F): ").strip().lower()

    if genero in ("m", "f"):
        break
    else:
        print("Gênero inválido. Digite 'M' para masculino ou 'F' para feminino.")

    
try:
    h = float(input("Digite sua altura: "))
except:
    print("Valor inválido!")
    exit()

match genero:
    case "M" | "m":
        resultado = (72.7*h) - 58
        print(f"Seu peso ideal é de: {round(resultado, 2)}")
    case "F" | "f":
        resultado = (62.1 *h) - 44.7
        print(f"Seu peso ideal é de: {round(resultado, 2)}")
        