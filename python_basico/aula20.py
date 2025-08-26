"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
nome = 'Victor'
valor = 1000.29345
variavel = '%s, o preço é R$%.2f' % (nome, valor)
print(variavel)
print('O hexadecimal de %i é %08x' % (15, 15))