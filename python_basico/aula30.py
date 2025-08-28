"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Tipos imutaveis: str, int, float, bool
"""
nome = 'Victor Hugo'
# Por uma str ser imutável isso gera um erro
# nome[3] = '123'
nome_modificado = f'{nome[:3]}123{nome[4:]}'
print(nome_modificado)