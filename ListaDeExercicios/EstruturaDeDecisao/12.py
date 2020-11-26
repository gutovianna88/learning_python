"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
hourly_wage = float(input("Informe o salario recebido por hora: "))
total_hours_worked = float(input("Qual o total de horas trabalhadas: "))
if hourly_wage * total_hours_worked <= 900:
    IR = 0
elif hourly_wage * total_hours_worked > 900 and hourly_wage <= 1500:
    IR = 5
elif hourly_wage * total_hours_worked > 1500 and hourly_wage <= 2500:
    IR = 10
elif hourly_wage * total_hours_worked > 2500:
    IR = 20
total_discounts = (hourly_wage * total_hours_worked * IR / 100) + (hourly_wage * total_hours_worked * 0.03)

print("Salario bruto: (", total_hours_worked, "* ", hourly_wage, ") : R$", hourly_wage * total_hours_worked)
print("(-) IR(", IR, "%): R$", hourly_wage * total_hours_worked * IR / 100)
print("(-) Sindicato (3 %): R$", hourly_wage * total_hours_worked * 0.03)
print("FGTS(11 %): R$", hourly_wage * total_hours_worked * 0.11)
print("Total de descontos: R$ ", total_discounts)
print("Salario Liquido: R$ ", hourly_wage * total_hours_worked - total_discounts)
