from random import randint
from time import sleep
print('{:=^21}'.format('Desafio 028'))
numero = randint(0, 5)
numerojog = int(input('De 0 a 5, qual numero estou pensando: '))
print('Analisando...')
sleep(1)
if numero == numerojog:
    print('Parabens, você acertou, eu pensei no numero {}'.format(numero))
else:
    print('você errou, eu pensei no numero {}'.format(numero))
