from random import randint
computador = randint(0, 100)
print('Sou seu computador...Eu pensei em um número entre 0 e 1000...')
print('Será que você consegue acertar?...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Número maior...Tente outra vez... ')
        elif jogador > computador:
            print('Número menor.Tente outra vez...')

print(f'Acertou com {palpites} tentativas...')
if palpites == 1:
    print('Você jogou com perfeição,PARABÈNS!!!')
elif palpites <= 5:
    print('Você jogou muito bem...')
elif palpites <= 10:
    print('Você jogou bem...')
else:
    print('Jogou mal,tente outra vez...')
