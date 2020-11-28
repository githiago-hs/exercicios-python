from datetime import date
print('{:=^21}'.format('Desafio 032'))
ano = int(input('Digite o ano para saber se ele é bissexto (Digite 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} NÃO é BISSEXTO'.format(ano))