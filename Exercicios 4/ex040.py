nota1 = float(input('Digite a primera nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'REPROVADO COM MEDIA {media}')
elif media >= 5 and media <= 6.9:
    print(f'RECUPERAÇÃO COM MEDIA {media}')
else:
    print(f'APROVADO COM MÉDIA {media}')
