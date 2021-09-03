while True:
    n = int(input('Qual o número que você deseja ver a tabuada: '))
    if n < 0:
        break
    print('*' * 30)
    for c in range(0, 11):
        print((f'{c} X {n} = {c * n}'))
    print('*' * 30)

print('-------------FIM-------------')
