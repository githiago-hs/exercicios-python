import datetime
year = datetime.date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = year - nasc
if idade > 18:
    print('Você está com {} anos e já deveria ter se alistado há {} ano(s) \nSeu alistamento foi em {}'.format(idade, idade - 18, nasc - (idade - 18)))
elif idade == 18:
    print('Você está com {} anos, vá até a junta militar mais próxima e se aliste já \nSeu alistamento é agora em {}'.format(idade, year))
else:
    print('Você está com {} anos, ainda não possui idade para se alistar, volte daqui há {} ano(s) \nSeu alistamento será em {}'.format(idade, 18 - idade, nasc + (18 - idade)))