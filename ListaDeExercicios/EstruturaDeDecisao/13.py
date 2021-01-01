"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""
number_week_day = int(input("Digite um numero de 1 a 7 para verificar o dia da semana: "))


if number_week_day == 1:
    print("Domingo")
elif number_week_day == 2:
    print("Segunda-feira")
elif number_week_day == 3:
    print("Terça-feira")
elif number_week_day == 4:
    print("Quarta-feira")
elif number_week_day == 5:
    print("Quinta-feira")
elif number_week_day == 6:
    print("Sexta-feira")
elif number_week_day == 7:
    print("Sabado")
else:
    print("Caractere invalido")
