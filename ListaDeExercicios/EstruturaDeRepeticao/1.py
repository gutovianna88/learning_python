"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""
score = 11 #Apenas um número que faça o loop ser executado.


while score > 10 or score < 0:
    score = float(input("Digite uma nova nota: "))

