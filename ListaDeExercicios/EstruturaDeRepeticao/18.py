"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
numbers = []
do_you_continue = True

while do_you_continue:
    adding_number = float(input("Digite o numero: "))
    numbers.append(adding_number)
    question = input("Voce quer digitar mais numeros [s/N]? ")
    if (question != "s"):
        do_you_continue = False


print(" Menor valor ", min(numbers), " Maior Valor ", max(numbers), " Soma ", sum(numbers))






"""
1. Coletar numeros ate cansar o usuario
2. Obter menor valor
3. Obter maior valor
4. Calcular a soma de infinite
"""