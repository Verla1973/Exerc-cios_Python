palavras = ('Verla', 'Amanda', 'Fernanda', 'Antonella')
for p in palavras:
    print(f'\nA palavra {p} tem as seguintes vogais: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}', end='')
