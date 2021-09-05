numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
           'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Numero inválido...Digite novamente...'))
    else:
        print(f'Você digitou o número {numeros[num]}...')
        break
print(sorted(numeros))
print(numeros.index('dezesseis'))
