"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
collection_cds = int(input("Informe o total de Cd's na coleção: "))
cds_price = []
cds_score = 0


while cds_score < collection_cds:
    price = int(input("Informe o valor do CD: "))
    cds_price.append(price)
    cds_score = cds_score +1


print("Total gasto: ", sum(cds_price), "| Gasto médio por CD: ", sum(cds_price)/cds_score)
