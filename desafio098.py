from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} indo de {p} em {p}...')
    sleep(3)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(2)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(2)
            cont -= p
        print('FIM!')


contador(0, 15, 1)
contador(16, -12, 1)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
