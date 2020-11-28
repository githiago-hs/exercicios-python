print('{:=^21}'.format('Desafio 031'))
dist = int(input('Digite a distância da viagem em Km: '))
if dist <= 200:
    print('A sua viagem é de {}Km e a passagem irá custar R${:.2f}'.format(dist, dist * 0.50))
else:
    print('A sua viagem é de {}Km e a passagem irá custar R${:.2f}'.format(dist, dist * 0.45))