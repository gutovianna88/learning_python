"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

integer_numbers = []
while len(integer_numbers) < 10:
    number = int(input("Digite mais um numero: "))
    integer_numbers.append(number)


even = []
odd = []

for each_number in integer_numbers:
    if (each_number % 2 == 0):
        even.append(each_number)
    elif (each_number % 2 > 0):
        odd.append(each_number)
print(len(even), "Par ", len(odd), "Impar ")




