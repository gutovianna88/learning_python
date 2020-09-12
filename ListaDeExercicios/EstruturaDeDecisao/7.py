"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
number_one = float(input("Digite o primeiro numero: "))
number_two = float(input("Digite o segundo numero: "))
number_three = float(input("Digite o terceiro numero: "))
if (number_one > number_two and number_one > number_three):
    print(number_one, "maior")
elif (number_two > number_one and number_two > number_three):
    print(number_two, "maior")
elif (number_three > number_one and number_three > number_two):
    print(number_three, "maior")


if (number_one < number_two and number_one < number_three):
    print(number_one, "menor")
elif (number_two < number_one and number_two < number_three):
    print(number_two, "menor")
elif (number_three < number_one and number_three < number_two):
    print(number_three, "menor")
