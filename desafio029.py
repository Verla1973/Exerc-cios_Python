vel = float(input('Digite a velocidade do carro: '))

if(vel <= 80):
    print('Parabéns...Você é um motorista exemplar...')
else:
    multa = vel - 80
    print('Você foi multado...')
    print('Sua velocidade ultrapassou o limite de velocidade da estrada...')
    print(f'Você estava a {vel}kmh...')
    print(f'Sua multa é de  R$ {multa * 7} ')
