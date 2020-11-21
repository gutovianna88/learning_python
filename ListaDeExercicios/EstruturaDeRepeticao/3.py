"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
name = input("Digite seu nome: ")
while len(name) <= 3:
    name = input("Digite o nome com mais de três caracteres: ")


age = int(input("Digite sua idade: "))
while age < 0 or age > 150:
    age = int(input("Digite a idade entre 0 e 150: "))


salary = int(input("Digite o seu salario: "))
while salary < 0:
    salary = int(input("Digite um salario maior que 0: "))


gender = input("Informe o sexo [f/m]: ")
while not (gender == "f" or gender == "m"):
    gender = input("Digite f para feminino e m para masculino: ")


marital_status = input("Informe o estado civil [s/c/v/d]: ")
while not (marital_status == "s" or marital_status == "c" or marital_status == "v" or marital_status == "d"):
    marital_status = input("Digite s para solteiro, c para casado, v para viuvo ou d para divorciado: ")


print("Nome: ", name, "Idade: ", age,"Anos", "Salario: ", salary, "Sexo: ", gender, "Estado civil: ", marital_status)