contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        print(f'Não vou mostrar o {contador}')
        # usamos o continue para voltar ao começo do laço
        continue

    if 10 <= contador <= 30:
        print(f'Não vou mostrar o {contador}')
        continue

    print(contador)

    if contador == 40:
        print(f'Chegamos no {contador}')
        # usamos o break para quebrar o laço
        break

print('Fim')
