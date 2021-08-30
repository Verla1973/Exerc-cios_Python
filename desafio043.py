nome = str(input('Digite seu nome: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / altura ** 2

if imc <= 18.5:
    print(f'Olá {nome.upper()}!!!')
    print(f'Você tem um indice de massa corporal igual a {imc:.2f}.')
    print('Você está abaixo do peso...')
elif imc <= 25:
    print(f'Olá {nome.upper()}!!!')
    print(f'Você tem um indice de massa corporal igual a {imc:.2f}.')
    print('Você está com um peso ideal...')
elif imc <= 30:
    print(f'Olá {nome.upper()}!!!')
    print(f'Você tem um indice de massa corporal igual a {imc:.2f}.')
    print('Você está com sobrepeso...')
elif imc <= 40:
    print(f'Olá {nome.upper()}!!!')
    print(f'Você tem um indice de massa corporal igual a {imc:.2f}.')
    print('Você está com obesidade...')
else:
    print(f'Olá {nome.upper()}!!!')
    print(f'Você tem um indice de massa corporal igual a {imc:.2f}.')
    print('Você está com obesidade mórbida...')
    print('Você já pode fazer um encaminhamento para cirúrgia de redução estomacal...')
