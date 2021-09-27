def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg}mts X {comp}mts é de: {a:.2f}mts²')


print('-=' * 15)
print('*****CONTROLE DE TERRENOS*****')
print('-=' * 15)
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)
