# Operações condicionais
entrada = input('Deseja entrar ou sair? ').upper()

if entrada == 'SAIR':
    print('Você saiu')
elif entrada == 'ENTRAR':
    print('Você entrou')
else:
    print('Resposta inválida')