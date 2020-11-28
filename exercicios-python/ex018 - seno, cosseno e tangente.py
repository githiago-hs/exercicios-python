from math import cos, sin, tan, radians
print('{:=^21}'.format('Desafio 018'))
angulo = int(input('Informe o angulo para saber o seno, cosseno e a tangente: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O seno é {:.2f} \n O cosseno é {:.2f} \n A tangente é {:.2f}'.format(sen, cos, tan))