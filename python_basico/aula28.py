horario = input('Que horas são: ')
horario_int = None

if horario.isdigit():
    horario_int = int(horario)

try:
    if 0 <= horario_int <= 11:
        print('Bom dia')
    elif 12 <= horario_int <= 17:
        print('Boa tarde')
    elif 18 <= horario_int <= 23:
        print('Boa noite')
except:
    print('Informe o horário corretamente')