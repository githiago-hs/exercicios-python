print('{:=^21}'.format('Desafio 029'))
vel = float(input('Digite a velocidade em Km/h: '))
if vel > 80:
    print('Sua velocidade foi de {}Km/h, você ultrapassou e 80km/h foi multado! Terá que pagar R${:.2f}'.format(vel, (vel-80) * 7.00 ))
else: 
    print('Sua velocidade está ok, siga em frente')