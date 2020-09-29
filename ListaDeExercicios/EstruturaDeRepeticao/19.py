"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

infinite = []
possibilites = float(input("Quantas variaveis gostaria de verificar? "))
while len(infinite) < possibilites:
    number = float(input("Digite um novo numero: "))
    if number > 0 and number < 1001:
        infinite.append(number)
    else:
        print("Valor incorreto! ")


print("Maior ", max(infinite), "Menor ", min(infinite), "Soma ", sum(infinite))