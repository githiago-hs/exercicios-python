print('{:=^21}'.format('Desafio 031'))
vcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
quantanos = int(input('Em quantos anos pretende pagar? '))
prestacao = vcasa / (quantanos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(vcasa, quantanos, prestacao))
if prestacao >= minimo:
    print('Infelizmente o empréstimo foi NEGADO!')
else:
    print('O seu empréstimo foi APROVADO!') 