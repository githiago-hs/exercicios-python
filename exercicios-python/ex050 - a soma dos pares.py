soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º numero: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você digitou {} valores pares, a soma entre eles é {}'.format(cont, soma))