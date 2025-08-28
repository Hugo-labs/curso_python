numero = input('Digite um número inteiro: ')
numero_int = None

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O número {numero_int} é par')
    else:
        print(f'O número {numero_int} é ímpar')
except:
    print('O valor digitado não é um número inteiro')

# if numero.isdigit():
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print('O número é par')
#     else:
#         print('O número é ímpar')
# else:
#     print('O valor digitado não é um número inteiro')