r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triangulo')
    if r1 == r2 and r1 == r3:
        print('Os segmentos formam um triangulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 == r2:
        print('Os segmentos formam um triangulo Isóceles')
    else:
        print('Os segmentos formam um triangulo Escaleno')
else:
    print('Os segmentos acima NÂO podem formar um triangulo')
