from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')

    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é: {soma}')
        sleep(5)
    elif opcao == 2:
        produto = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {produto}...')
        sleep(5)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O número {maior} é o maior...')
            sleep(5)
        elif n1 < n2:
            maior = n2
            print(f'O número {maior} é o maior...')
            sleep(5)
        else:
            print(f'Não há maior entre {n1} e {n2}.Os dois tem o mesmo valor...')
            sleep(5)
    elif opcao == 4:
        print('Digite novos números: ')
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite o segundo valor: '))

print('Processando...')
sleep(5)
print('Fim do programa...Volte sempre...')
