from time import sleep
m = 0


def maior(* num):
    print('\nAnalisando os números passados...')
    cont = maior = 0
    for valor in num:
        print(f'{valor} ', end='')
        sleep(3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores...')
    print(f'\nO maior valor informado foi {maior}...')


maior(2, 3, 7, 5, 9, 10)
maior(3, 1, 8, 6)
print('-=' * 20)
