print('{:=^21}'.format('Desafio 027'))
nome = str(input('Digite o seu nome completo: ')).strip().split()
print('Analisando... O seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Analisando... O seu ultimo nome é {}'.format(nome[len(nome) -1 ].capitalize()))