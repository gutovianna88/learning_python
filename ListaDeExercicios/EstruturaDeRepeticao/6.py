"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""
my_list = range(1, 21)
for item in my_list:
    print(item)


for item in my_list:
    print(item, end="|")
