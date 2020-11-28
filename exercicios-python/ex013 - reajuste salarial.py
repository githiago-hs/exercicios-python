print('{:=^21}'.format('Desafio 013'))
#Calculo salario do Funcionario
nomefun = str(input('Digite o nome do funcionário: '))
salario = float(input('Digite o salario atual do funcionário(use ponto ao invés de virgula): R$'))
aumento = salario * (15/100)
novosalario = salario + aumento
print('O novo salario de {:.2f} será de R${:.2f}'.format(salario, novosalario))
