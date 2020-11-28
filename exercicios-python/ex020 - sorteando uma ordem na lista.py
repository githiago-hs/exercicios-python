from random import shuffle
print('{:=^21}'.format('Desafio 20'))
al1 = str(input('Digite o nome do aluno(a): '))
al2 = str(input('Digite o nome do aluno(a): '))
al3 = str(input('Digite o nome do aluno(a): '))
al4 = str(input('Digite o nome do aluno(a): '))
lista = [al1, al2, al3, al4]
#ordem = random.sample(lista, k=len(lista))
shuffle(lista)
print('A sequencia dos trabalhos segue da seguinte forma {}'.format(lista))