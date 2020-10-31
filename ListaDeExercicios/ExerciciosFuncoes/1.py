"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""

def numeric_pyramid(number):
    if number.isnumeric():
        number = int(number)


        for i in range(1, number +1):
            for k in range(i):
                print(i, end= " ")
            print()


    else:
        print("Caractere ínvalido ")


ask_number = input("Indique um numero: ")
numeric_pyramid(ask_number)
