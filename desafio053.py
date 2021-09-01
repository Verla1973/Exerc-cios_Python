frase = str(input('Digite ua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de: {junto}, é: {inverso}')
if junto == inverso:
    print('Temos um Palíndromo..,')
else:
    print('A frase digitada não é um palíndromo...')
