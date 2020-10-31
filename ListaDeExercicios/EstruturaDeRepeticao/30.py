"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
 que já é um sucesso na sua loja de 1,99.
 Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães,
 a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
"""
from decimal import Decimal


bread_price = input("Digite o valor unitario do pão: ")
bread_price = bread_price.replace(",", ".")
validation = bread_price.replace(".", "")


def format_money(money):
    return  "R$ {:.2f}".format(money)


def two_digits(number):
    number_str = str(number)
    return number_str.zfill(2)


if validation.isnumeric():
    bread_price = float(bread_price)
    for single in range(1, 51):
        calc = single * bread_price
        print(two_digits(single), " - ", format_money(calc))

else:
    print("Valor não permitido! ")
