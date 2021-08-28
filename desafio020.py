import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)
print(f'A ordem de apresentação dos trabalhos ficou assim: ')
print(lista)
