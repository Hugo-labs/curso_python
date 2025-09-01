# while/else

str = 'Ola chuchus'

i = 0

while i < len(str):

    # Na presença de algo que interrompa a execução total do while, o else não será executado
    break

    print(str[i])
    i += 1

else:
    print('Else executado')

print('Fim')
