"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
first_brand = input(" Qual a primeira marca? ")
first_price_brand = float(input("Qual o preço da primeira marca a ser comparada? "))
second_brand = input(" Qual a segunda marca? ")
second_price_brand = float(input("Qual o preço da segunda marca a ser comparada? "))
third_brand = input(" Qual a terceira marca? ")
third_price_brand = float(input(" Qual o preço da terceira marca a ser comparada? "))
if (first_price_brand < second_price_brand and first_price_brand < third_price_brand):
    print(first_brand, first_price_brand)
elif (second_price_brand < first_price_brand and second_price_brand < third_price_brand):
    print(second_brand, second_price_brand)
else:
    print(third_brand, third_price_brand)

