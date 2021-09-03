cont = soma = 0
while True:
    num = int(input('Digite um valor(999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'A soma dos números foi: {soma}...')
print(f'Ao total foram digitados {cont} números...')
print('-=' * 10)
print('-------FIM--------')
