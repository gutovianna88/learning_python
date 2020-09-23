"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""
number_one = int(input("Insira o primeiro numero: "))
number_two = int(input("Insira o segundo numero: "))
intervalos = range(number_one + 1, number_two)
contra = range(number_two + 1, number_one)
for interval in intervalos:
    if(number_one < number_two):
        print(interval)
else:
        for newcontra in contra:
            if(number_one > number_two):
                print(newcontra)





