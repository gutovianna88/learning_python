"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
 e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
  “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
first_grade = float(input("Digite a primeira nota do semestre: "))
second_grade = float(input("Digite a segunda nota do semestre: "))
average_grade = (first_grade + second_grade)/2


if average_grade >= 9.0 and average_grade <= 10.0:
    print("Primeira nota: ", first_grade, "Segunda nota: ", second_grade,"Média: ", average_grade, "Nota A! ", "APROVADO")
elif average_grade >= 7.5 and average_grade <= 8.9:
    print("Primeira nota: ", first_grade, "Segunda nota: ", second_grade,"Média: ", average_grade, "Nota B! ", "APROVADO")
elif average_grade >= 6.0 and average_grade <= 7.4:
    print("Primeira nota: ", first_grade, "Segunda nota: ", second_grade,"Média: ", average_grade, "Nota C! ", "APROVADO")
elif average_grade >= 4.0 and average_grade <= 5.9:
    print("Primeira nota: ", first_grade, "Segunda nota: ", second_grade,"Média: ", average_grade, "Nota D! ", "REPROVADO")
elif average_grade >= 0.0 and average_grade <= 3.9:
    print("Primeira nota: ", first_grade, "Segunda nota: ", second_grade,"Média: ", average_grade, "Nota E! ", "REPROVADO")