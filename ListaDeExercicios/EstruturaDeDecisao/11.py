"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input(" Digite seu salario: "))
if(salario <= 280.00):
    print(" Salario anterior", salario, " Aumento de 20% ", "Valor do aumento ", (salario * 20)/100, " / ", " NOVO SALARIO", salario + ((salario * 20)/100))
elif(salario > 280.00 and salario <= 700.00):
    print(" Salario anterior", salario, " Aumento de 15% ", "valor do aumento ", (salario * 15)/100, " / ", " NOVO SALARIO", salario + ((salario * 15)/100))
elif(salario > 700.00 and salario <= 1500.00):
    print(" Salario anterior", salario, " Aumento de 10% ", "valor do aumento ", (salario * 10)/100, " / ", " NOVO SALARIO", salario + ((salario * 10)/100))
elif(salario > 1500):
    print(" Salario anterior", salario, " Aumento de 5% ", "Valor do aumento ", (salario * 5)/100, " / ", " NOVO SALARIO", salario + ((salario * 5)/100))

