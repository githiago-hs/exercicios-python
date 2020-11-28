s1 = float(input('Primeiro seguimento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1: 
    print('Essas retas PODEM formar um triangulo')
    if s1 == s2 and s1 == s3 and s2 == s3:
        print('Seus segmentos formam um triângulo EQUILÁTERO')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print('Seus segmentos formam um triângulo ISÓSCELES')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('Seus segmentos formam um triangulo ESCALENO')
else:
    print('Essas retas NÃO PODEM formar um triangulo')