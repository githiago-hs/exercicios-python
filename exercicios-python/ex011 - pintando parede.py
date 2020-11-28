print('{:=^21}'.format('Desafio 011'))
#Calculo de area
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A quantidade de tinta necessária para pintar {} metros quadrados é de {} Litros'.format(area, tinta))
