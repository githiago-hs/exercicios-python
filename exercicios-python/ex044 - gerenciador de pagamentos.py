print('{:=^21}'.format('LOJAS GUANABARA'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))
if opcao == 1: 
    print('Sua compra terá um desconto de 10% portanto custará R${:.2f}'.format(preco - preco*10/100))
elif opcao == 2:
    print('Sua compra terá um desconto de 5% portanto custará R${:.2f}'.format(preco - preco*5/100))
elif opcao == 3:
    print('Você escolheu pagar em 2x no cartão, portanto sua compra não terá desconto, você irá pagar o valor original de R${:.2f}'.format(preco))
elif opcao == 4:
    parcela = int(input('Em quantas parcelas deseja pagar? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, preco/parcela))
    print('Portanto sua compra de R${:.2f} custará R${:.2f} no final.'.format(preco, preco + preco*20/100))
else:
    print('Opção inválida')