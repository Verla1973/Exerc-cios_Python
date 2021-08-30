# Simulador simples de empréstimo

valor_casa = float(input('Digite o valor da casa que deseja financiar: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Digite em quantos anos deseja pagar o financiamento: '))
parcelas = anos * 12
valor_parcelas = valor_casa / parcelas
porcentagem_comprometida = salario * 0.30
if valor_parcelas < porcentagem_comprometida:
    print(f'Valor da casa é R$ {valor_casa}...')
    print(f'Você financiando em {parcelas} parcelas,o valor mensal ficará em R$ {valor_parcelas:.2f}')
    print(f'CRÉDITO APROVADO!PARABÈNS PELA COMPRA DE SUA CASA PRÓPRIA...')
else:
    print('CRÉDITO NEGADO POR VALOR DA PARCELA EXCEDER OS 30% DO SALÁRIO...')
