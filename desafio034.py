# programinha para calcular o aumento de salário de funcionários
# baseado no salário atual,sendo que salários abaixo de R$ 1250,00
# receberão aumento de 15% e salários acima disto,receberão
# aumento de 10%
print('X' * 45)
salario_atual = float(input('Digite o salário do funcionário: '))
if(salario_atual <= 1250):
    salario_novo = (salario_atual * 0.15) + salario_atual
    print(f'O salário do funcionário era de R$ {salario_atual},com o aumento de 15%')
    print(f'o salário do funcionário ficou em R$ {salario_novo}...')
else:
    salario_novo = (salario_atual * 0.10) + salario_atual
    print(f'O salário do funcionário era de R$ {salario_atual},com o aumento de 10%')
    print(f'o salário do funcionário ficou em R$ {salario_novo}...')
