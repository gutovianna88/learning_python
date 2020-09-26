"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex: 5!=5.4.3.2.1=120
"""

factorial_number = int(input("Digite o numero a ser verificado o fatorial: "))
predecessors = range(1, factorial_number)
predecessors = reversed(predecessors)

calc = factorial_number

for predecessor in predecessors:
    calc = calc * predecessor


print(calc)


