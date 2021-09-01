soma = 0
cont =0
for num in range(0, 500 + 1):
    if num % 2 == 1 and num % 3 == 0:
        cont = cont + 1
        soma = soma + num
print(f'A soma de todos os {cont} números solicitados foi: {soma}...')
