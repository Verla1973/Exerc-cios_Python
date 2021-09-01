soma = 0
for num in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
print(soma)
print('**FIM**')
