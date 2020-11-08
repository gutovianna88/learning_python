"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""
def verification_number(number):
    if type(number) is float:
        if number > 0:
            return "P"
        else:
            return "N"
    else:
        return False


n = input("Informe um numero: ")
n1 = n.replace("-","")
if n1.isnumeric():
    n = float(n)
    print(verification_number(n))
else:
    print("Caractere invalido! ")