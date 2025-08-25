"""
Operador lógico in e not in
str são iteráveis
 0 1 2 3 4 5
 V i c t o r
-6-5-4-3-2-1
"""
# nome = 'Victor'
# print(nome[2])
# print('c' in nome)
# print('tor' in nome)
# print('Vic' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('O que deseja encontrar no nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')