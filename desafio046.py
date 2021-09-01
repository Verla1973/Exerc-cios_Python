# contagem regressiva
from time import sleep
marcador = int(input('Digite o tempo(segundos) que deseja iniciar a contagem: '))
for marcador in range(marcador, -1, -1):
    print(f'Tempo: {marcador} segundos...')
    sleep(1)
print('Fim...')
print('FELIZ ANO NOVO!!!!')
