from random import choice
print('{:=^21}'.format('Desafio 019'))
al1 = str(input('Digite o nome do aluno(a): '))
al2 = str(input('Digite o nome do aluno(a): '))
al3 = str(input('Digite o nome do aluno(a): '))
al4 = str(input('Digite o nome do aluno(a): '))
escolha = choice([al1, al2, al3, al4])
print('Quem irá apagar o quadro será... {}'.format(escolha))