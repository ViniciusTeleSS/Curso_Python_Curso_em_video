import math as ma

angulo = float(input('Digite um angulo: '))

seno = ma.sin(ma.radians(angulo))
cosseno = ma.cos(ma.radians(angulo))
tangente = ma.tan(ma.radians(angulo))

print(f'O seno de {angulo} é {seno:.2f}')
print(f'O cosseno é {cosseno:.2f}')
print(f'E a tangente é {tangente:.2f}')
