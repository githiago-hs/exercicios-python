numero = int(input('Digite um numero inteiro: '))
opcao = int(input('Em qual base numerica deseja converter: \n [1] converter para BINÁRIO \n [2] converter para OCTAL \n [3] converter para HEXADECIMAL \n Sua opção: '))
if opcao == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida')