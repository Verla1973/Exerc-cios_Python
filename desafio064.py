num = cont = soma = 0
num = int(input('Digite um número[999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número[999 para parar]: '))
print(f'Você digitou {cont} e a soma deles foi {soma}...')
print('******FIM******')
