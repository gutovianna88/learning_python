"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""
number_one = float(input("Informe o numero base: "))
number_two = float(input("Informe o numero de elevação: "))

i = 0
calc = number_one

while(i < number_two):
    calc = (calc * number_one)
    i = i + 1 # i += 1 tambem poderiamos escrever dessa forma

print(calc)