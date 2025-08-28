nome = input('Seu nome: ').strip().title()
tamanho_nome = len(nome)

if tamanho_nome == 0:
    print('Você não digitou nada')
elif  1 <= tamanho_nome <= 4:
    print('Seu nome é curto')
elif 5 <= tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('O seu nome é longo')
