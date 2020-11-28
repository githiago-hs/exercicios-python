peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2) 
print('O seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso, alimente-se melhor')
elif imc > 18.5 and imc <= 25:
    print('Parabéns, voce está no peso IDEAL!')
elif imc > 25 and imc <= 30:
    print('Você está com SOBREPESO, cuidado!')
elif imc > 30 and imc <= 40:
    print('CUIDADO, você está com OBESIDADE')
else:
    print('CUIDADO! Você está com OBESIDADE MÓRBIDA')