"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
number_one = float(input("Primeiro numero: "))
number_two = float(input("Segundo numero: "))
number_three = float(input("Terceiro numero: "))
numbers = (number_one, number_two, number_three)
number_organized = sorted(numbers)
number_organized.reverse()
print (number_organized)
