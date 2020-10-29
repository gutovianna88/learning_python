"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""
classes = int(input("Informar a quantidade de turmas a serem consideradas: "))
total_classes = 0
students_grids = []


while total_classes < classes:
    class_by_class = int(input("Informe a quantidade de alunos a considerar para esta turma: "))
    if class_by_class <= 40:
        students_grids.append(class_by_class)
        total_classes = total_classes +1
    else:
        print("Quantidade acima da permitida! ")
student_media = sum(students_grids)/ classes


print(" Média de alunos por turma ", student_media)

