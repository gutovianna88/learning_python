"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

numero_escolha = float(input("Escolha um numero qualquer que lhe direi se é positivo ou negativo:"));
if(numero_escolha>0):
	print("Positivo!");
elif(numero_escolha==0):
	print("Zero!");
elif(numero_escolha<0):
	print("Negativo!");
