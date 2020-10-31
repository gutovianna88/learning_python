"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
total_collection = int(input("Qual o total de CDs de sua coleção? "))
collection = range(1, total_collection +1)
total_price = []


for itens in collection:
    price = int(input("Qual o valor deste item? "))
    total_price.append(price)


print("Custo total de CD's: ", sum(total_price), "| Custo médio por CD: ", sum(total_price) / total_collection)

