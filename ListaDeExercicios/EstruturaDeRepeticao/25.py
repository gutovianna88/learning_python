"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
ages = []
question = "s"


while question == "s":
    personalage = input("Digite a idade de um dos membros: ")
    ages.append(personalage)
    question = input("Ha novas idades a serem verificadas? [s/N] ")


young = []
adult = []
old = []
for age in ages:
    if age < "26":
        young.append(age)
    elif age >= "26" and age <= "60":
        adult.append(age)
    elif age > "60":
        old.append(age)


if len(young) > len(adult) and len(young) > len (old):
    print("A maioria grupo é jovem ")
elif len(adult) > len(young) and len(adult) > len(old):
    print("A maioria do grupo é adulto ")
elif len(old) > len(young) and len(old) > len(adult):
    print("A média a maioria do grupo é idoso ")

