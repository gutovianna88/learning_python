"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""
def tax_calculation(price, tax1):
    return (tax1 / 100)*price + price

initial_price = float(input("Informe o valor inicial para acrescentarmos o imposto: "))
tax = float(input("Informe a taxa de imposto que deverá ser acrescentada: "))


print("Valor inicial: ", initial_price, "Taxa de Imposto: ", tax, "Novo valor: ", tax_calculation(initial_price, tax))



# 1 Solicitar o valor
# 2 solicitar taxa de imposto
# 3 utilizar função para calcular o imposto
# 4 Imprimir valor anterior, taxa de imposto, valor calculado do imposto e valor total