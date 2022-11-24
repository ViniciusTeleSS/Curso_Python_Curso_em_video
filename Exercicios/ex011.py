larg = float(input('Digite a largura da parede em M '))
alt = float(input('Digite a altura da mesma parede em M '))
areaparede = larg * alt
tinta = areaparede / 2

print(
    f'Sua parede tem a dimensão de {larg} X {alt} e sua área é de {areaparede:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')
