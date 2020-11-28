print('{:=^21}'.format('Desafio 034'))
nome = str(input('Digite o nome do funcionário: ')).strip()
sal = float(input('Digite o salário do funcionário: R$'))
if sal > 1250.00:
    print('O salário de {} terá um aumento de 10%, portanto o novo salario de {} será de R${:.2f}'.format(nome.capitalize(), nome.capitalize(), sal + (sal * 10/100)))
if sal <= 1250.00:
    print('O salário de {} terá um aumento de 15%, portanto o novo salario de {} será de R${:.2f}'.format(nome.capitalize(), nome.capitalize(), sal + (sal * 15/100)))
