"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M.
como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""
def validation_and_parse_hour(hour):
    if hour.isnumeric():
        return  int(hour)

    print("Caractere inválido!")
    exit()


def validation_and_parse_minute(minute):
    if minute.isnumeric():
        return int(minute)

    print("Caractere inválido!")
    exit()



def hour_conversion(hour):
    if hour > 12:
        return hour - 12

    return hour


def day_time(hour):
    if hour < 12:
        return "AM"

    return "PM"

info_hour = input("Por favor informar o horario no formato de 24h (hh): ")
info_minute = input("Por favor informar os minutos (mm): ")

info_hour = validation_and_parse_hour(info_hour)
info_minute = validation_and_parse_minute(info_minute)

print(hour_conversion(info_hour), ":", info_minute, day_time(info_hour))

