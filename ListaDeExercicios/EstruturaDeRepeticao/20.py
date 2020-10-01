"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""
cont = True
while cont:
    factorial_number = int(input("Digite o numero a ser verificado o fatorial: "))
    if (factorial_number > 0 and factorial_number > 16):
        predecessors = range(1, factorial_number)
        predecessors = reversed(predecessors)
        calc = factorial_number
        for predecessor in predecessors:
            calc = calc * predecessor
        print("Resultado ", calc)
        what = input("Voce quer calcular outro fatorial? [s/N] ")
        if (what != "s"):
            cont = False


