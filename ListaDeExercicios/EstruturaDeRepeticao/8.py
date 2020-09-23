"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
my_list = []
while len(my_list) < 5:
    print("Informe o novo numero ")
    new_number = float(input())
    my_list.append(new_number)


print("soma " , sum(my_list), "Média ", sum(my_list)/len(my_list))