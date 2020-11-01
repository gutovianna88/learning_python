print("1- soma");
print("2- multiplicacao");
print("3- divisao");
print("4- subtrai");
primeiro_numero = float(input("primeiro_numero?"));
segundo_numero = float(input("Qual segundo numero?"));
operacao = input("O que quer meu rei?");


if (operacao =="1"):
    print(primeiro_numero + segundo_numero);
elif (operacao =="2"):
    print(primeiro_numero * segundo_numero);
elif (operacao =="3"):
    print(primeiro_numero / segundo_numero);
elif (operacao =="4"):
    print(primeiro_numero - segundo_numero);
else:
    print("Operação invalida");