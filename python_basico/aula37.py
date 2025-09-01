# Calculadora com while

# numero_1 = None
# numero_2 = None
# float_numero_1 = None
# float_numero_2 = None
# operador = None
operadores_validos = ['+', '-', '*', '/']

print('Escreva sair para encerrar')
# laço para o programa executar infinitamente
while True:
    # primeira variável verificando também se deseja interromper o programa
    numero_1 = input('Número 1: ').upper()
    if numero_1 == 'SAIR':
        break

    # segunda variável, também fazendo a verificação
    numero_2 = input('Número 2: ').upper()
    if numero_2 == 'SAIR':
        break

    # parte responsável por verificar se os valores inseridos foram números ou não e convertendo para float
    float_numero_1 = 0
    float_numero_2 = 0

    try:
        float_numero_1 = float(numero_1)
        float_numero_2 = float(numero_2)
    
    except:
        print('Digite um número válido')
        continue


    # entrada do operador que será utilizado
    operador = input('Deseja + - / *: ')

    while operador not in operadores_validos:
        if len(operador) > 1:
            operador = input('Digite apenas um operador: ')
        else: 
            operador = input('Deseja + - / *: ')

    # resolução das contas
    # soma
    if operador == '+':
        soma = float_numero_1 + float_numero_2
        print(f'{float_numero_1} + {float_numero_2} = {soma}')
    # subtração
    elif operador == '-':
        subtracao = float_numero_1 - float_numero_2
        print(f'{float_numero_1} - {float_numero_2} = {subtracao}')
    # multiplicação
    elif operador == '*':
        multiplicacao = float_numero_1 * float_numero_2
        print(f'{float_numero_1} x {float_numero_2} = {multiplicacao}')
    # divisão
    elif operador == '/':
        divisao = float_numero_1 / float_numero_2
        print(f'{float_numero_1} / {float_numero_2} = {divisao}')

print('Fim')
