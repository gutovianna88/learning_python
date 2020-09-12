"""
Faça um Programa que leia três números e mostre o maior deles.
"""
number_one = float(input("Digite o primeiro numero: "))
number_two = float(input("Digite o segundo numero: "))
number_three = float(input("Digite o terceiro numero: "))
if(number_one > number_two and number_one > number_three):
    print(number_one)
elif(number_two > number_one and number_two > number_three):
    print(number_two)
else:
    print(number_three)
