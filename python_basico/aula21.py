"""
formatação básica de str
"""
variavel = 'ABCD'
print(variavel)

# Para adicionar um determinado número de espaços a esquerda 
print(f'{variavel:_>10}')

# Para adicionar espaços a direita
print(f'{variavel:_<10}')

# Para deixar no centro e adicionar espaços em ambos os lados
print(f'{variavel:_^10}')

# Para definir o número de casas decimais que será exibida de um número com ponto flutuante
# Podemos inserir a vírgula para separar as casas decimais a esquerda do ponto em milhares 
print(f'{1000.2234523262:_=+10,.2f}')

# Para exibir o exadecimal de um determinado valor
print(f'O hexadecimal de 1500 é {1500:08x}')