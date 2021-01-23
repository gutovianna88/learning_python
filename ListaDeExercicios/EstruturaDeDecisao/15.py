"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
 Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
side_a_test = ""
while not side_a_test.isnumeric():
    side_a = input("Digite o tamanho do lado A :")
    side_a_test = side_a.replace(".", "")


side_b_test = ""
while not side_b_test.isnumeric():
    side_b = input("Digite o tamanho do lado B :")
    side_b_test = side_b.replace(".", "")


side_c_test = ""
while not side_c_test.isnumeric():
    side_c = input("Digite o tamanho do lado C :")
    side_c_test = side_c.replace(".", "")

side_a = float(side_a)
side_b = float(side_b)
side_c = float(side_c)

if side_a == side_b and side_a == side_c:
    print("Triangulo equilatero")
elif side_a == side_b or side_a == side_c:
    print("Triangulo Isosceles")
else:
    print("Triangulo Escaleno")
