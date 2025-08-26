"""
Fatiamento de str
"""

frase = 'Hello World'

# fatiamento [i:f:p]
# i - inicio do fatiamento 
print(frase[1:])
print(frase[6:])

# f - fim do fatiamento 
print(frase[:5])
print(frase[6:11])

# p - passo, quantas casas irá pular
numeros = '0123456789'
print(numeros[::2])

# len - retorna a quantidade de caracteres da str
print(len(frase))
print(len(numeros))