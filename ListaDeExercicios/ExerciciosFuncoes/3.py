"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""
def sum_three_numbers(number_one, number_two, number_three):
    if (type(number_one) is int and
        type(number_two) is int and
        type(number_three) in int):
        calc = number_one + number_two + number_three
        return calc
    else:
        return False


three_numbers = []
while len(three_numbers) < 3:
    number = input("Informe um numero: ")
    if number.isnumeric():
        number = int(number)
        three_numbers.append(number)
    else:
        print("Condição aceita apenas numeros!! ")


calc = sum_three_numbers(three_numbers[0], three_numbers[1], three_numbers[2])
if calc == False:
    print("Os itens digitados não são validos! ")

else:
 print(calc)


