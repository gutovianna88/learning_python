"""
Faça um programa que peça 4 numeros para o usuário e retorne a soma de todos eles;
"""

numbers_list = []
number_one = float(input(" Digite o primeiro numero da lista: "))
number_two = float(input(" Digite o segundo numero da lista: "))
number_three = float(input(" Digite o terceiro numero da lista: "))
number_four = float(input("Digite o quarto numero da lista: "))
numbers_list.append(number_one)
numbers_list.append(number_two)
numbers_list.append(number_three)
numbers_list.append(number_four)

# Forma Imperativa = voce que faz

sumatory = 0
for number in numbers_list:
    print("antes", sumatory)
    sumatory = sumatory + number
    print("depois", sumatory)
    print("fim desse exec")

print(sumatory)


"""
 -- Forma declarativa = ta pronta --

print("Total ", sum(numbers_list))
"""
