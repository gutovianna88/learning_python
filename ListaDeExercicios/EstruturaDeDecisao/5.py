"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota_um = float(input("Primeira Nota: "));
nota_dois = float(input("Segunda Nota: "));
calc = ((nota_um + nota_dois)/2);
if(calc == 10):	
	print("Aprovado com distinção");
elif(calc >= 7):	
	print("Aprovado");
else:
	print("Reprovado");
