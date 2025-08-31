nome = input('Digite o seu nome: ')
novo_nome = ''
contador = 0

while contador < len(nome):
    novo_nome += f'*{nome[contador]}'
    contador += 1
novo_nome += '*'

print(novo_nome)
