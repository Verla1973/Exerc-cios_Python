a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# Testando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

# Testando o maior valor
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O maior valor digitado foi: {maior}...')
print(f'O menor valor digitado foi: {menor}...')
