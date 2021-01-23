"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro
valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o
programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações
pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da
prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""
paid_on_the_day = []
current_value = -1


def valorPagamento(value,days):
    if not type(value) is float or type(value) is int:
        print("Digite valores validos [0.00] :")
        return False


    if not type(days) is int:
        print("Digite valores validos [00]")
        return False


    if days == 0:
        return value

    return (value * 0.03) + (value * 0.001)* days + value


while current_value != 0:
    current_value = input("Digite o valor da fatura: ")
    current_value = float(current_value)
    if current_value != 0:
        delayed_days = input("Digite a quantidade de dias em atraso: ")
        delayed_days = int(delayed_days)
        new_value = valorPagamento(current_value, delayed_days)
        paid_on_the_day.append(new_value)
        print(new_value)

print("Valor Total de prestações pagas: R$", sum(paid_on_the_day))
print("Quantidade Total de prestações pagas: ", len(paid_on_the_day))

