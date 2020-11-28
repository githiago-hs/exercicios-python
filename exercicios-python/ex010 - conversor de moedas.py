print('{:=^21}'.format('Desafio 010'))
#conversor de moedas
real = float(input('Digite a quantidade em reais que deseja converter: R$'))
dolar = real / 3.27
print('Com R${:.2f} você poderá comprar US${:.2f}'.format(real, dolar))