print('#' * 45)
kms = float(input('Digite os kilometros da viagem: '))
if kms <= 200:
    print(f'Sua viagem de {kms}kms vai custar um total de R$ {kms * 0.50}...')
else:
    print(f'Sua viagem de {kms} kms,vai custar um total de R$ {kms * 0.45}...')
print('#' * 45)
