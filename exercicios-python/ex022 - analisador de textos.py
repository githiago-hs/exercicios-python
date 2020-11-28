print('{:=^21}'.format('Desafio 022'))
nome = str(input('Digite o seu nome: '))
mai = nome.upper()
minu = nome.lower()
espacos = nome.count(' ')
totalletras = len(nome) - espacos
totprinome = nome.split()

print("""Letras Maiúsculas: {}
    Letras Minúsculas: {}
    Total de letras: {}
    Total de letras primeiro nome: {}""".format(mai, minu, totalletras, len(totprinome[0])))