from math import hypot

catetoOP = float(input('Qual é o comprimento do Cateto Oposto? '))
catetoAD = float(input('Qual é o comprimento do Cateto Adjacente? '))
hipotenusa = hypot(catetoOP, catetoAD)

print(f'O comprimento da hipotenusa é de {hipotenusa:.2f}')
