"""
Operador lógico or
or - Qualquer condição verdadeira, avalia toda a expressão como verdadeira
"""
senha = '123456'
entrada = input('[E]ntrar [S]sair: ')
senha_digitada = input('Senha: ')

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha:
    print('Entrou')
else:
    print('Saiu')