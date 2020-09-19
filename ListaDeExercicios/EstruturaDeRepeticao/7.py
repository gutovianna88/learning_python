"""
Faça um programa que leia 5 números e informe o maior número.
"""
the_five = []
while len(the_five) < 5:
    print("Proximo numero: ")
    um_dos = float(input())
    the_five.append(um_dos)


print("Maior numero: ", max(the_five))
