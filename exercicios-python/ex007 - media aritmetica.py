print('{:=^21}'.format('Desafio 007'))
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota de {}: '.format(nome)))
nota2 = float(input('Digite a segunda nota de {}: '.format(nome)))
media = (nota1 + nota2) / 2
print('A media de {} é: {:.2f}'.format(nome, media))
