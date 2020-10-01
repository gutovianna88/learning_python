"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""
number = int(input("Digite um numero para verificar se este numero é primo: "))
if number % 2 >= 1:
    print("Primo ")
else:
    print("Não é primo ")
