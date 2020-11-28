print('{:=^21}'.format('Desafio 012'))
#Calculo de desconto
preco = float(input('informe o preço do produto(use ponto ao invés da virgula): R$'))
desconto = preco * (5 / 100)
novopreco = preco - desconto
print('O produto com 5% de desconto vai custar {:.2f}'.format(novopreco))