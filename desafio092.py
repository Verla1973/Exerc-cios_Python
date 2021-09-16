from datetime import datetime
dados = {}
dados['nome'] = str(input('Qual o seu nome? '))
nasc = int(input('Digite seu ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['sexo'] = str(input('Qual seu sexo: ')).strip().upper()[0]
dados['ctps'] = int(input('Carteira de trabalho: (digite 0 se não tiver CTPS)'))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Digite seu salário: '))
    if dados['sexo'] == 'M':
        dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 35) - datetime.now().year
    else:
        dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 30) - datetime.now().year
print('*' * 30)
for k, v in dados.items():
    print(f'{k} : {v}...')
