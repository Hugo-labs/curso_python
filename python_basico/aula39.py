frase = 'O Python é uma linguagem de programação multiparadgma ' \
        'Python foi criado por Guido Von Rossum.'

i = 0
letra_mais_repetida = None
qtd_letra_mais_repetida = 0
letra_atual = ''

while i < len(frase):
    # Responsável por pular os espaços vazios
    if frase[i] == ' ':
        i += 1
        continue

    # Contagem de quantas vezes determinada letra aparece na frase
    letra_atual = frase[i]
    qtd_letra_atual = frase.count(letra_atual)

    # Usado para atribuir a primeira letra e sua quantidade, as variaveis que usaremos
    if letra_mais_repetida == None:
        letra_mais_repetida = letra_atual
        qtd_letra_mais_repetida = qtd_letra_atual
    
    # Onde defini qual letra mais foi repetida
    if qtd_letra_atual > qtd_letra_mais_repetida:
        letra_mais_repetida = letra_atual
        qtd_letra_mais_repetida = qtd_letra_atual

    # print(letra_atual)
    # print(qtd_letra_atual)

    i += 1

print(f'A letra mais repetida foi "{letra_mais_repetida}" e ela apareceu {qtd_letra_mais_repetida}')