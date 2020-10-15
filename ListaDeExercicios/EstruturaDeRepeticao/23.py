"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""
number = int(input("Digite um numero para verificar se é primo e informar os numeros primos anteriores a ele: "))
if number % 2 >=1:
    print("Numero Primo")
else:
    print("Numero não é primo")
numbers = range(1, number)
primenumbers = []
for numberinnumber in numbers:
    if numberinnumber % 2 >=1:
        primenumbers.append(numberinnumber)


print("Numeros Primos anteriores: ", primenumbers, "Numero de divisões realizadas: ", len(numbers)+1)
