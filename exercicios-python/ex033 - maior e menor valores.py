print('{:=^33}'.format('Desafio 033'))
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))
if num1 > num2 and num1 > num3:
    print('Dos numeros digitados o numero {} é o maior'.format(num1))
if num2 > num1 and num2 > num3: 
    print('Dos numeros digitados o numero {} é o maior'.format(num2))
if num3 > num1 and num3 > num2: 
    print('Dos numeros digitados o numero {} é o maior'.format(num3))
if num1 < num2 and num1 < num3:
    print('E o menor é o {}'.format(num1))
if num2 < num1 and num2 < num3:
    print('E o menor é o {}'.format(num2))
if num3 < num2 and num3 < num1:
    print('E o menor é o {}'.format(num3))