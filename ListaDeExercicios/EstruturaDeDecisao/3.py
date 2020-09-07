"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

print("M - Masculino");
print("F - Feminino");
qual_sexo = input("Qual seu sexo?");
if(qual_sexo =="M"):
	print("Masculino");
elif(qual_sexo =="F"):
	print("Feminino");
else:
 print("Inválido");
