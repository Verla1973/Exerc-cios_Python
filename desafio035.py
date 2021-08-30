print('*' * 45)
print('Analisador de triângulos')
print('*' * 45)

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM formar um triângulo...')
else:
    print('Os segmentos acima NÃO podem formar um triângulo...')
