print('CADASTRE UMA PESSOA')

maior_idade = 0
homens = 0
mulheres = 0

while True:

    idade = input('Idade: ')
    while not idade.isdigit():
        idade = input('Idade: ')
    numero = int(idade)

    sexo = input('Sexo [M/F]: ').upper()
    while sexo not in ('F', 'M'):
        sexo = input('Sexo [M/F]: ').upper()

    cont = input('Quer continuar? [S/N]: ').upper()
    while cont not in ('S', 'N'):
        cont = input('Quer continuar? [S/N]: ').upper()

    if numero > 18:
        maior_idade += 1

    if sexo in 'M':
        homens += 1

    if numero < 20 and sexo in 'F':
        mulheres += 1

    if cont == 'N':
        break

print('FIM DO PROGRAMA\n')
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
