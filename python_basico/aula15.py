primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f'O {int_primeiro_valor=} é maior que o {int_segundo_valor=}')
elif int_segundo_valor > int_primeiro_valor:
    print(f'O {segundo_valor=} é maior que o {int_primeiro_valor}')
else:
    print('Os valores são iguais')
