"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
number_one = int(input("Insira o primeiro numero: "))
number_two = int(input("Insira o segundo numero: "))
intervalos = range(number_one + 1, number_two)
contra = range(number_two + 1, number_one)
sumatory_intervalos = 0
sumatory_contra = 0
for interval in intervalos:
    if(number_one < number_two):
        sumatory_intervalos = sumatory_intervalos + interval
print(sumatory_intervalos)

for newcontra in contra:
    if(number_one > number_two):
        sumatory_contra = sumatory_contra + newcontra
print(sumatory_contra)