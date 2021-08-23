reais = float(input('Quantos reais você possui: '))
dolar = 3.27
dolar_comprado = (reais / dolar)

print(f'Olá, você falou que possue {reais} reais...')
print(f'Com esses reais você consegue comprar {dolar_comprado:.2f} dólares...')
