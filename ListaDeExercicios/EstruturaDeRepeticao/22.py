"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
"""
number = int(input("Digite um numero para verificar se este numero é primo: "))
if number % 2 >= 1:
    print("Primo ")
else:
    divisors = range(1, number + 1)
    consensus_division = []
    for divisor in divisors:
        if number % divisor == 0:
            consensus_division.append(divisor)
    print(consensus_division)

