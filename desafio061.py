from time import sleep
print('---Gerador de PA---')
print('-=' * 12)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
print('Processando...')
sleep(3)
while cont <= 10:
    print(f'{termo}...')
    sleep(3)
    termo += razao
    cont += 1
print('*******FIM*******')
