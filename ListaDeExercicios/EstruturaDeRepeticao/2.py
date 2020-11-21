"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

user_name = "0"
pswd = "0"


while user_name == pswd:
    user_name = input("Digite um nome de usuario: ")
    pswd = input("Digite uma senha (não repetir o nome de usuario): ")

