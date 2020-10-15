"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
grades = []
question = "s"
while question == "s":
    print("Digite a nota: ")
    grade = float(input())
    grades.append(grade)
    question = input("Deseja digitar uma nova nota? [s/N] ")
print(sum(grades)/len(grades))