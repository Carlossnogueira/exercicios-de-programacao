"""
Faça um programa para pagamento de comissão de vendedores de peças, levando-se em consideração que sua 
comissão será de 5% do total da venda e que você tem os seguintes dados: 
- Identificação do vendedor 
- Código da peça 
- Preço unitário da peça 
- Quantidade vendida 
"""

indentificacao = str(input("Digite o código do vendedor: "))
codigo = int(input("Digite o código da peça: "))
preco = float(input("Digite o preço da peça: "))
quantidade = int(input("Digite a quantidade de peças: "))

resultado = preco * quantidade
comicao = resultado * 0.05

print("----- Recibo de Comissão -----")
print(f"Vendedor: {indentificacao}")
print("Código da peça: {}".format(codigo))
print("Total da venda: R$ {}".format(round(resultado,2)))
print("Comissão (5%): R$ {}".format(round(comicao,2)))