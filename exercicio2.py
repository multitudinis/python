# Faça um programa que pergunte a hora ao usuario, de acordo com a hora,
# o programa deve responder bom dia, boa tarde ou boa noite

horario = input("Digite a hora agora (0-23): ")

try:
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print("Bom Dia!")
    elif horario >= 12 and horario <= 18:
        print("Boa Tarde!")
    elif horario >= 19 and horario <= 23:
        print("Boa Noite!")
    else:
        print("Digite apenas o numero correspondente as horas, sem os minutos")
except:
    print("Digite apenas o numero correspondente as horas, sem os minutos")
