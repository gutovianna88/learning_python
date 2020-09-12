"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letter = input("Digite uma letra para que o sistema verifique se é vogal ou consoante: ")
letter = letter.lower()
if(not letter.isalpha()):
    print("O valor não é uma letra!")
    quit(0)


if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
    print("Vogal")
else:
    print("Consoante")




