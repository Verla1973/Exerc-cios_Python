from time import sleep
print('---Gerador de PA---')
print('-=' * 12)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
print('Processando...')
sleep(3)
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}...')
        sleep(3)
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos mais você deseja mostrar? '))
print(f'Progressão finalizada com {total} termos mostrados')
print('*******FIM*******')
