"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
newlist = range(1, 51)
for newitem in newlist:
    if (newitem % 2 > 0):
        print(newitem)