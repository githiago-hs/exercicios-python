from math import hypot
print('{:=^21}'.format('Desafio 017'))
co = float(input('Informe o cateto oposto do triangulo: '))
ca = float(input('Informe o cateto adjacente do triangulo: '))
print('De acordo com os valores passados, a hipotenusa desse triangulo é {}'.format(hypot(co, ca)))